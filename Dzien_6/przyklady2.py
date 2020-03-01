class Pojazd:

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def poruszaj_sie(self):
        print("Porusza sie")

    def stop(self):
        print("Pojazd zatrzymal się")

class Statek(Pojazd):

    def plyn(self):
        self.poruszaj_sie()
        print("Płynie ...")

class Samochod(Pojazd):

    def jedz(self):
        self.poruszaj_sie()
        print("Jedzie ...")

class Amfibia(Statek, Samochod):

    def __init__(self, nazwa, typ):
        super().__init__(nazwa)
        # Statek.__init__(self, nazwa)
        self.typ = typ

prom = Statek("Batory")
prom.plyn()
prom.stop()

samochod = Samochod("Ford")
samochod.jedz()
samochod.stop()

amfibia = Amfibia("Lola", "Wojskowa")
amfibia.jedz()
amfibia.plyn()
amfibia.stop()



class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
