class Produkt:
    def __init__(self, id: int, nazwa: str, cena: float):
        self.id =  id
        self.nazwa = nazwa
        self.cena = cena
        self.vat = round(self.cena * 0.23,2)

    def __str__(self):
        return f"<Produkt o numerze id {self.id} to {self.nazwa}. Jej cena wynosi {self.cena}, w tym {self.vat} vat"

    def print_info(self):
        print(f"<Produkt o numerze id {self.id} to {self.nazwa}. Jej cena wynosi {self.cena}, w tym {self.vat} vat")

product =Produkt(1,"Woda", 10.99)
product2 = Produkt(2,"Kawa", 15)

product.print_info()

