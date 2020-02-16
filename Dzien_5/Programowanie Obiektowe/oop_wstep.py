class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return f"<Osoba {self.imie}>"


os1 =Osoba("Paweł")
os1.imie = "Paweł"
os2 =Osoba("Bob")
os2.imie = "Bob"

print(os1)
print(dir(os1))
print(type(os1))