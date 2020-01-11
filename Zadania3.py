liczba = int(input("Podaj liczbę :"))

try:
	print()
	print(f"Większa od 10 {liczba>10}")
	print(f"Mniejsza, równa 15 {liczba<=15}")
	print(f"Podzielna przez 2 {liczba%2==0}")
except:
	print("coś poszło nie tak")