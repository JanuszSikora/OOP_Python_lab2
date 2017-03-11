from time import sleep
import pickle,shelve

class Konto:
    total=0
    @staticmethod
    def licznik():
        return Konto.total
    
    def __init__(self,wlasciciel,numer,saldo):
        self.wlasciciel=wlasciciel
        self.numer=numer
        self.saldo=saldo
        Konto.total+=1
        
    def __str__(self):
        self.Info()
        return str(self.informacja)

    def Info(self):
        self.informacja='Konto: ',self.wlasciciel,' nr: ',self.numer,' o saldzie: ',round(self.saldo,2)
        return self.informacja

    #zapis obiektów do pliku
    def plik_zapisz(self,objekt):
        pickle.dump(objekt,plik_konta)

    #zapamiętanie ilości obiektów w oddzielnym pliku
    def il_objektow(self,il_kont):
        plik_konta_dl=open('konta_plik_dl.dat','wb')
        pickle.dump(il_kont,plik_konta_dl)
        plik_konta_dl.close()

    #odczyt ilości obiektów z pliku
    def plik_czytaj_il_kont(self):
        plik_konta_dl=open('konta_plik_dl.dat','rb')
        il_kont=pickle.load(plik_konta_dl)
        plik_konta_dl.close()
        self.il_kont=il_kont
        return self.il_kont

    #odczyt obiektów z pliku
    def plik_czytaj_konta(self):
        plik_konta=open('konta_plik.dat','rb')
        il_kont=self.plik_czytaj_il_kont()
        if il_kont!=0:
            for i in range(il_kont):
                konta_firm.append(pickle.load(plik_konta))
            plik_konta.close()
        else:
            print('Liczba kont=0')


class Prywatne(Konto):
    def __init__(self,wlasciciel,numer,saldo,):
        super().__init__(wlasciciel,numer,saldo,)
        self.Info()

           
class Firmowe(Konto):
    def __init__(self,wlasciciel,numer,saldo):
        super().__init__(wlasciciel,numer,saldo)
        self.Info()

    def ZUS(self):
        self.zaplac=float(input('Podaj kwotę ZUS do zapłaty: '))
        self.saldo-=self.zaplac
        self.Info()
        return self.informacja

    def PIT(self):
        self.zaplac=float(input('Podaj kwotę PIT do zapłaty: '))
        self.saldo-=self.zaplac
        self.Info()
        return self.informacja


  
#main
konta_firm=[]

#Tworzenie obiektów 'konta prywatne'
#konto1=Prywatne('ja','003',2.10)
#konto3=Prywatne('ty','123',12.10)
#konto4=Prywatne('on','333',24.25)


#Tworzenie obiektów 'konta firmowe'
konta_firm.append(Firmowe('oni','34',22.33))
konta_firm.append(Firmowe('my','0034',102))
konta_firm.append(Firmowe('wy','1234',222.22))
konta_firm.append(Firmowe('nowy','123400',10))


for i in range(Konto.total): 
    print(konta_firm[i])#wyświetlenie danych konta przed operacją zapłaty ZUS/PIT
    konta_firm[i].ZUS()
    konta_firm[i].PIT()
    print(konta_firm[i])#wyświetlenie danych konta po operacji zapłaty ZUS/PIT

#zapis obiektów do pliku - operacja jednorazowa, potem "za-#-owane"
konta_firm[0].il_objektow(Konto.total)
plik_konta=open('konta_plik.dat','wb')
for i in range (Konto.total):
   konta_firm[i].plik_zapisz(konta_firm[i])
plik_konta.close()

#odczyt z pliku metodą klasy
dummy=Konto('wywolanie_metody','001',0.1)
il_kont=dummy.plik_czytaj_il_kont()
dummy.plik_czytaj_konta()

for i in range (il_kont):
    print(konta_firm[i])

sleep(2)

