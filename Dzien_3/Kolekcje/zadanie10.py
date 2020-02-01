napis = input("Napisz coś: ")
znaki = {}
for z in napis:
    znaki[z] = znaki.get(z,0)+1


for l  in znaki:
    print(f"Znak  {l} w napisie {napis} występuje {znaki[l]} razy")

print()


from collections import defaultdict


for z in napis:
    znaki[z] +=1


for l  in znaki:
    print(f"Znak  {l} w napisie {napis} występuje {znaki[l]} razy")