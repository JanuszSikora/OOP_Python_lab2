from time import sleep


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        self.info()
        return str(self.informacja)

    def info(self):
        self.informacja = 'Dane osobowe; imie: ', self.imie, ' nazwisko: ', self.nazwisko
        return self.informacja


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, nr_pracownika):
        super().__init__(imie, nazwisko)
        self.nr_pracownika = nr_pracownika

    def info(self):
        self.informacja = 'Dane osobowe; imie: ', self.imie, ' nazwisko: ', self.nazwisko, 'nr_pracownika', \
                          self.nr_pracownika
        return self.informacja


class Wyplata (Pracownik):
    def __init__(self, imie, nazwisko, nr_pracownika):
        super().__init__(imie, nazwisko, nr_pracownika)
        lista_wyplat = []
        self.lista_wyplat = lista_wyplat

    def wyplac(self, kwota_wyplaty): # nr_pracownika,
        self.lista_wyplat.append(kwota_wyplaty)
        return self.lista_wyplat

    def info(self):
        self.informacja = 'Lista wypłat pracownika nr ', self.nr_pracownika, 'to: ', self.lista_wyplat
        return self.informacja


# main
# Tworzenie obiektów
osoba_1 = Osoba('George','Bush')
osoba_2 = Osoba('Jakis','Tam')
pracownik_1 = Pracownik('Jan', 'Kowal', '0021')
pracownik_2 = Pracownik('Ela', 'Nowak', '211')
wyplata_pracownika_1 = Wyplata(pracownik_1.imie, pracownik_1.nazwisko, pracownik_1.nr_pracownika)
wyplata_pracownika_2 = Wyplata(pracownik_2.imie, pracownik_2.nazwisko, pracownik_2.nr_pracownika)

print(pracownik_1, '\n', pracownik_2)

# ewidencja wypłat wynagrodzeń dla poszczególnych pracowników
wyplata_pracownika_1.wyplac(200)
wyplata_pracownika_1.wyplac(400)
wyplata_pracownika_2.wyplac(600)
wyplata_pracownika_1.wyplac(1100)
wyplata_pracownika_2.wyplac(2000)

print(wyplata_pracownika_1)
print(wyplata_pracownika_2)

sleep(2)
