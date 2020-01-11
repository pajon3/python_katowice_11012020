liczba = int(input("Podaj liczbę :"))

print(f"Liczba spełnia warunki: {liczba%2==0 and liczba%3==0 and liczba>10 or liczba == 7}")
