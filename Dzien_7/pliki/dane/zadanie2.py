import sys
if len(sys.argv)>1:
    plik = sys.argv[1]
else:
    plik= "emails.txt"



try:
    x = 1
    with open(plik) as f:
        for line in f:
            print(x, line[:-1])
            x +=1
except FileNotFoundError:
    print("nie znalazłem pliku")


