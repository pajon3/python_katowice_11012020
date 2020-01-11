# 01_TypyLiczbowe.py
#plik pythonowy nazywamy modułem

#liczby całkowite - int
#funkcja do sprawdzania typu:
print(type(1))

#uruchomienie skryptu: 
#python nazwa modułu .py

#operacje i operatory
print(1+1)
print(1-1)
print(1*2)
print(1/2) # dzielenie zwyczajne
print(1//2) # zwraca liczbę całkowitą
print(1%2) # zwraca resztę z dzielenia
print(2**3) #potęga	
print(pow(2,3)) # inna potęga	
print(3>4)
print(4==2*2)
print(3*3!=2)# 

#wartości logiczne z dużel litery
# wszystko co nie jest zerem ani pustym jest True
print(type(True))

print(1_000_000) # po prostu milion

print(0b101010) #system dwójkowy
print(0o12342) #system ósemkowy
print (0x123abc) #szesnastkowy


#zmienne:
#	nie mogą się zaczynać od cyfr
#	tylko liczby, litery i znaki podkreślenia
#	nie może być to słowo kluczowe

nazwa_zmiennej = "wartość"
_ = 10


#liczby zmienno przecinkowe (float)
0.11

from decimal import Decimal

print(Decimal("0.1")+Decimal("0.1")+Decimal("0.1") ==Decimal("0.3"))


#complex - liczby zespolone






















