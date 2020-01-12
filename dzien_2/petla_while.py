i = 0

while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

print("="*40)

while i>0:
    print(i)
    i = i-1
    if i == 6:
        print("STOP")
        break