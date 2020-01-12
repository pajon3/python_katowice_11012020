#PYGAME do stworzenia planszy

import random

wymiar = 10
skarb_x = random.randint(1,wymiar)
skarb_y = random.randint(1,wymiar)
gracz_x = random.randint(1,wymiar)
gracz_y = random.randint(1,wymiar)
los = 0
x = 0
y = 0
odleglosc = abs(gracz_y- skarb_y)+abs(gracz_x-skarb_x)
odleglosc_min = odleglosc
ruchy = 0

while True:
    print(f"znajdujesz się na pozycji: {gracz_x}x{gracz_y}")
    if skarb_x == gracz_x and skarb_y == gracz_y:
        print("znalazłeś skarb ")
        if ruchy>1:
            print(f"Zrobiłeś {ruchy} ruchów")
        elif ruchy ==0:
            print("Nawet nie musiałeś ruszać się z miejsca")
        else:
            print(f"Zrobiłeś {ruchy} ruch")
        break
    ruch = input("Wprowadź ruch: ")
    if ruch  == "w":
        gracz_y += 1
    elif ruch  == "s":
        gracz_y -= 1
    elif ruch == "a":
        gracz_x += 1
    elif ruch  == "d":
        gracz_x -= 1
    ruchy += 1
    if any([gracz_x>wymiar, gracz_x<0,gracz_y>wymiar,gracz_y<0]) == True:
        print("Jesteś poza planszą, przegrałeś")
        break
    if random.randint(1,5) == 5:
        print("tym razem nie dostaniesz wskazówki")
    else:
         if abs(gracz_y- skarb_y)+abs(gracz_x-skarb_x)>odleglosc:
            print("źle")
         else:
            print("dobrze")
    odleglosc = abs(gracz_y- skarb_y)+abs(gracz_x-skarb_x)

    if ruchy>=2*odleglosc_min:
        skarb_x = random.randint(1, wymiar)
        skarb_y = random.randint(1, wymiar)
        odleglosc_min = odleglosc
        ruchy = 0
        print("skarb został przeniesiony")
    print()









