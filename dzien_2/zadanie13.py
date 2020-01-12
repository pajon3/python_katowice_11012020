
i = 1
y = 0

while i<=7:
    x = int(input("wprowadź temperaturę w dniu nr " + str(i)))
    y = y + x
    i += 1

print(round(y/7,2))

