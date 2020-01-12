lista = [14,29,-29,-10,-92,3,-21]
ujemne = 0
dodatnie = 0

for el in lista:
    if el >0:
        dodatnie += 1
    elif el<0:
        ujemne +=1
print("""
Liczby dodatnie: {}
Liczby ujemne: {}
""".format(dodatnie,ujemne))