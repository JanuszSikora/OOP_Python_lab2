from time import sleep
import pickle


class Konto:
    total = 0
    saldo_ma = 0
    saldo_wn = 0

    @staticmethod
    def licznik():
        return Konto.total

    @staticmethod
    def przelew(kwota, saldo_wn, saldo_ma, msc_przelewu):
        saldo_ma += kwota
        saldo_wn -= kwota
        Konto.saldo_wn = saldo_wn
        Konto.saldo_ma = saldo_ma
        return Konto.saldo_wn, Konto.saldo_ma

    # zapis obiektów do pliku
    @staticmethod
    def plik_zapisz():
        plik_konta = open('konta_plik4.dat', 'wb')
        k=0
        for i in lista_kont:
            pickle.dump(i, plik_konta)
            k+=1
        plik_konta.close()
        plik_konta_dl = open('konta_plik4_dl.dat', 'wb')
        pickle.dump(k, plik_konta_dl)
        plik_konta_dl.close()

    def __init__(self, wlasciciel, numer, saldo):
        self.wlasciciel = wlasciciel
        self.numer = numer
        self.saldo = saldo
        Konto.total += 1

    def __str__(self):
        self.info()
        return str(self.informacja)

    def info(self):
        self.informacja = 'Konto: ', self.wlasciciel, ' nr: ', self.numer, ' o saldzie: ', round(self.saldo, 2)
        return self.informacja

    # odczyt ilości obiektów z pliku
    def plik_czytaj_il_kont(self):
        plik_konta_dl = open('konta_plik4_dl.dat', 'rb')
        il_kont = pickle.load(plik_konta_dl)
        plik_konta_dl.close()
        self.il_kont = il_kont
        return self.il_kont

    # odczyt obiektów z pliku
    def plik_czytaj_konta(self):
        plik_konta = open('konta_plik4.dat', 'rb')
        il_kont = self.plik_czytaj_il_kont()
        if il_kont != 0:
            for i in range(il_kont):
                lista_kont.append(pickle.load(plik_konta))
            plik_konta.close()
        else:
            print('Liczba kont=0')


class Obrotowe(Konto):
    def __init__(self, wlasciciel, numer, saldo):
        super().__init__(wlasciciel, numer, saldo)


class Oszczedn(Konto):
    def __init__(self, wlasciciel, numer, saldo, msc_ostat_przelewu):
        super().__init__(wlasciciel, numer, saldo)
        self.msc_ostat_przelewu = msc_ostat_przelewu

    def info(self):
        self.informacja = 'Konto oszczędnościowe: ', self.wlasciciel, ' nr: ', self.numer, ' o saldzie: ', \
                          round(self.saldo, 2), 'ostatni przelew z tego konta był w mscu', self.msc_ostat_przelewu
        return self.informacja


# main
lista_kont=[]

# Tworzenie obiektów 'konta obrotowe' - przy odczycie kont z pliku za-#-ować
konto_obr_1 = Obrotowe('ja','003',2220.10)
konto_obr_2 = Obrotowe('ty','123',12.10)
konto_obr_3 = Obrotowe('on','333',24.25)

# Tworzenie obiektów 'konta oszczędnościowe' - przy odczycie kont z pliku za-#-ować
konto_oszcz_1 = Oszczedn('oni','34',1022.33,1)
konto_oszcz_2 = Oszczedn('my','0034',10200,3)
konto_oszcz_3 = Oszczedn('wy','1234',2222.22,5)

# dodawanie wszystkich kont do jednej listy - przy odczycie kont z pliku za-#-ować
lista_kont.append(konto_obr_1)
lista_kont.append(konto_obr_2)
lista_kont.append(konto_obr_3)
lista_kont.append(konto_oszcz_1)
lista_kont.append(konto_oszcz_2)
lista_kont.append(konto_oszcz_3)

# odczyt z pliku metodą klasy - przy tworzeniu listy obiektów-kont za-#-ować
#dummy = Konto('wywolanie_metody', '001', 0.1)
#il_kont=dummy.plik_czytaj_il_kont()
#dummy.plik_czytaj_konta()

# stan kont przed operacją przelewu
for i in lista_kont:
    print(i)

# wykonanie przelewu
numer_wn = str(input('Podaj konto, z którego ma być dokonany przelew: '))
numer_ma = str(input('Podaj konto, na które ma być dokonany przelew: '))
msc_przelewu = int(input('Podaj miesiąc wykonania przelewu: '))
numer_wn_obj = ''
numer_ma_obj = ''

for i in lista_kont:
    if numer_wn == i.numer:
        saldo_wn = i.saldo
        konto_wn = i
        numer_wn_obj = i.numer
        try:
            msc_ostat_przelewu = i.msc_ostat_przelewu
            while msc_przelewu < 1 or msc_przelewu > 12 or msc_ostat_przelewu == msc_przelewu or msc_ostat_przelewu> \
                    msc_przelewu:
                if msc_przelewu < 1 or msc_przelewu > 12:
                    msc_przelewu = int(input('Podaj miesiąc wykonania przelewu - liczbę pomiędzy 1 a 12: '))
                elif msc_ostat_przelewu == msc_przelewu:
                    msc_przelewu = int(input('W jednym miesiącu możliwy jest tylko jeden przelew z konta '
                                              'oszczędnościowego - podaj inny miesiąc'))
                else: # while msc_ostat_przelewu > msc_przelewu:
                    msc_przelewu = int(input('Miesiąc przelewu nie może być wcześniejszy niż poprzedni przelew z konta '
                                          'oszczędnościowego - podaj inny miesiąc'))
            odsetki_msc = (2.0/12/100) # odsetki założone "na sztywno" 2.0%/Y
            saldo_wn = saldo_wn*(1+odsetki_msc*(msc_przelewu-msc_ostat_przelewu))
            i.msc_ostat_przelewu = msc_przelewu
        except:
            pass

    if numer_ma == i.numer:
        saldo_ma = i.saldo
        konto_ma = i
        numer_ma_obj = i.numer
if numer_wn_obj == '':
    print('Nie ma takiego konta wn')
if numer_ma_obj == '':
    print('Nie ma takiego konta ma')
if numer_wn_obj == '' or numer_ma_obj == '':
    pass
else:
    kwota = 0
    while kwota <= 0:
        kwota = float(input('Podaj kwotę do zapłaty: '))
    Konto.przelew(kwota, saldo_wn, saldo_ma, msc_przelewu)
    konto_wn.saldo = Konto.saldo_wn
    konto_ma.saldo = Konto.saldo_ma

Konto.plik_zapisz()

# stan kont po operacji przelewu
for i in lista_kont:
    print(i)

sleep(2)
