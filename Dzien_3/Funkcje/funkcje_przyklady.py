def kwardaty(n):
    return [i**2 for i in range (n)]

print(kwardaty(2))
print(kwardaty(4))
print(kwardaty(10))

def hello():
    print("Hello")

hello()

def sumuj(a,b):
    print(a,b)
    print(a+b)

sumuj(12,23)


## zasiegi

a = 1

print(locals())
print(globals())

def incr_a():
    a = 10
    print(locals())
    print(globals())

incr_a()
print("a", a)

