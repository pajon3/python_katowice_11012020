h = int(input("Podaj wysokość :"))
a = int(input("Podaj długość :"))
b = int(input("Podaj szerokość :"))

v = a*b*h
czy_wieksze_od_litra = v>1000

print(f"Czy większe od litra?: {czy_wieksze_od_litra}")