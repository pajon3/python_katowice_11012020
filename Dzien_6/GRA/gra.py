"""
Na dole moje komentarze ;)
"""

##################################################################################################
# importy itp
##################################################################################################
from faker import Faker

fake = Faker("pl_PL")


##################################################################################################
# Klasy
##################################################################################################
class Player:

    def __init__(self, name):
        self.name = name
        self.life = fake.random.randint(1, 100)
        self.attack = fake.random.randint(1, 20)
        self.defence = fake.random.randint(1, 10)
        self.equipment = []
        self.experience = 0
        self.location = Location.random_position()

    def __str__(self):
        return f"<{self.name}| life:{self.life},attack:{self.attack} defence:{self.defence}>"

    def alive(self):
        if self.life > 0:
            return True
        else:
            return False

    def get_hurt(self, hit):
        hitx = min(hit, self.life)
        if fake.random.randint(0, 20) < self.defence:
            print(f"Opponent's attack missed the target.  Remaining life: {self.life}")
        else:
            self.life -= hitx
            print(f"{self.name} got hurt with {hitx} points. Remaining life: {self.life}")

    def strike(self):
        force = fake.random.randint(0, self.attack())

    def take_weapon(self, weapon):
        self.equipment.append(weapon)
        self.attack += weapon.attack_bonus
        print(f"What a luck. You picked {weapon.name}. Your attack is increased by {weapon.attack_bonus} points.")

    def take_armor(self, armor):
        self.equipment.append(armor)
        self.defence += armor.defence_bonus
        print(f"You found {armor.name} your defence is increased by {armor.defence_bonus} points. Good for you!")

    def take_potion(self, potion):

        if potion.recovery == 0:
            print("Potion appeared to be a poison. You are dead.")
            self.life = 0
        else:
            recoveryx = min(potion.recovery, 100 - self.life)
            self.life += recoveryx
            print(f"{recoveryx}Potion has healed you. Remaining life: {self.life}")

    @staticmethod
    def creature_combat(player, creature):
        while player.alive and creature.alive:
            creature.get_hurt(player.strike())
            print(f"{player.name} strikes {creature.name}")
            player.get_hurt(creature.attack)
            print(f"{creature.name} strikes {player.name}")
            print(player)
            print(creature)
        if not player.alive:
            return False
        else:
            return True

class Potion:
    def __init__(self):
        self.recovery = fake.random.randint(0, 50)
        self.location = Location.random_position()


class Weapon:
    def __init__(self, name):
        self.attack_bonus = fake.random.randint(0, 20)
        self.name = name
        self.location = Location.random_position()

class Armor:

    def __init__(self, name):
        self.name = name
        self.defence_bonus = fake.random.randint(1,5)
        self.location = Location.random_position()

class Creature:
    def __init__(self, name, life, attack, agression):
        self.name = name
        self.agression = agression
        self.attack  = fake.random.randint(1, attack)
        self.life = life
        self.location = Location.random_position()

    def get_hurt(self, force):
        forcex = max(force, self.life)
        self.life -= force

    def alive(self):
        if self.life> 0:
            return True
        else:
            return False




    def __str__(self):
        return f"<{self.name} |attack: {self.attack}, life: {self.life}>"

class Location:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def w(self):
        self.y +=1
    def s(self):
        self.y -=1
    def a(self):
        self.x -=1
    def d(self):
        self.x +=1

    @classmethod
    def random_position(cls):
        return cls(fake.random.randint(1,10), fake.random.randint(1,10))

    def __str__(self):
        return f"{self.x, self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y







##################################################################################################
# wprowadzanie danych postaci itp
##################################################################################################


p1 = Player("Wielki Wojownik")
pot1 = Potion()
w1 = Weapon("Birch Sword")
a1 = Armor("Moss Armor")
c1 = Creature("Wolf",20,10, True)

##################################################################################################
# rozgrywka
##################################################################################################

print(p1)
print(a1.name, a1.location)
print(c1.name, c1.location)
print(w1.name, w1.location)
print("Potion", pot1.location)



while p1.alive:
    print(p1.location)
    direction = input(f"Where to go? (wasd)")
    try:
        getattr(p1.location, direction)()
    except AttributeError:
        print("WASD!!!")

    if p1.location  == a1.location:
        p1.take_armor(a1)
        a1.location = Location(100,100)
        print(p1)

    elif p1.location == w1.location:
        p1.take_weapon(w1)
        w1.location = Location(100,100)
        print(p1)

    elif p1.location == pot1.location:
        p1.take_potion(pot1)
        pot1.location = Location(100,100)
        print(p1)

    elif p1.location == c1.location:
        result = Player.creature_combat(p1, c1)
        if result is True:
            print(f"You killed a {c1.name}. Your experience is increased by x (Sorry, demo version)")
        else:
            break






if p1.alive():
    "That was a hard day on Earth. Try not to be killed tommorow"
else:
    "Game Over"


"""
Opis gry:
Na planszy 10x10 pojawia się postać, zbroja, broń eliksir oraz jakiś stwór

Gracz(postać) może poruszać się po planszy, otrzymywać obrażenia oraz atakować. 
Jeżeli gracz otrzyma uderzenie losowana jest wartośc od 1 do 20. Jeżeli jest niższa niż obrona gracza, cios nie dosięga celu.
Gracz może poprawić swoją orone poprzez podniesienie zbroi schowanej gdzieś na planszy. 
Gracz może zaatakowac przeciwnika z moca przyjmujacą wartości losowe od 1 do siły ataku gracza.
Siła może byc zwiększona poprzez podniesienie broni.
Gracz może się uleczyć poprzez znalezielnie eliksiru. Eliksir leczy losowo od 1 do 50 punktów życia lecz tak aby zdrowie gracza nie przekroczyło 100 punktów.
w 2% przypadków eliksir okazuje sie trucizna i gracz ginie.

Co nie działa:
System walki. Niestety cały czas otrzymuje bład  TypeError: 'int' object is not callable i na razie nie potrafie zauważyc gdzie leży problem

Co jeszcze nie jest napisane:
Testy. Zajmę się nimi w najbliższym czaasie, kiedy poprawię system walki.

Możliwość uniknięcia walki. Jeżeli napotkane stworzenie jest agresywne to zawsze wywiąze się walka, jeżeli nie, będzie możliwość ucieczki
Doświadczenie. Jakiś prosty mechanizm, który zwiększy doświadczenie postaci po odbytej walce. Doświadczenie może podwyższyc poziom a wtedy wzrastaja statystyki postaci. 

Co jest do nauczenia:

Wydaje mi się ze rozumiem już jak działają klasy. Natomiast użyte @staticmethod i @classmethod w większości przepisałem. Jeszcze nie rozgryzłem do końca po co one sa i jak ich używać.
Czy mogę prosic o jakieś nowe polecenie, które mógłbym dołożyc do tej gry, a które wymagałyby użycia tych komend?
  
"""