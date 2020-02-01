# Suma                    |
# róznica                 _
# część wspólna           &
# suma - część wspólna    ^

print(set)
print(set())
print(set([1,2,3,4]))

x= set("abdehata")

x.add("z")

for i in x:
    print(i)

A = {1,2,3,4}
B = {3,4,5,6}

print(A|B)
print(A-B)
print(A&B)
print(A^B)