from time import sleep

class Zwierze:
    def __init__(self,imie):
        self.imie=imie
            

    def Odglos(self,dzwiek):
        self.dzwiek=dzwiek
        print(self.imie,self.dzwiek)


class Pies(Zwierze):
    def __init__(self,imie):
        super().__init__(imie)
        self.Odglos('Hau')


class Kot(Zwierze):
    def __init__(self,imie):
        super().__init__(imie)
        self.Odglos('Miau')

    
#main
zoo=[Pies('Azor'),Kot('Tosia'),Pies('Shisha'),Kot('Max')]


sleep(2)

