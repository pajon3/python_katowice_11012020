"""
Stwórz klasę Postac
która ma atrybuty
- zycie
- sila
- zwinnosc
- obrona
- imie

Stworz klase przedmioty, któ

*Przy użyciu biblioteki Faker stwórz mechanizm tworzenia losowych postaci
(pip install faker)

postać w czasie tworzenia umiejscowania jest na planszy

"""
from faker import Faker
fake = Faker("pl_PL")

class Postac:

    def __init__(self, name, zycie, sila, zwinnosc, obrona):
        self.name = name
        self.zycie = fake.random.randint((1,101))
        self.sila = fake.random.randint((1,101))
        self.zwinnosc = fake.random.randint((1,101))
        self.obrona = fake.random.randint((1,101))

    @ classmethod
    def with_fake_name(cls):
        return cls(fake.name())

    def __str__(self):
        return f"<{self.name}| e: {zycie},e: {sila},e: {zwinnosc},e: {obrona}>"

    postac = Postac("Zenek")
    print(postac)

    def zadaj_obrazenia(self):
        return fake.random.randint(1,self.sila)


class Polozenie:
    def init(self,x,y):
        self.x =x
        self.y =y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    @classmethod
    def  random(cls):



 class Przedmiot:
     def __init__(self, name, typ):
