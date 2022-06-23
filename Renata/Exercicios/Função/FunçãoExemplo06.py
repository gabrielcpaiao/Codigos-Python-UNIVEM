from random import randint

def geraLista():
    L = []
    for i in range(10):
        L.append(randint(1,50))
    return L

a = geraLista()
print(a)
b = geraLista()
print(b)
c = geraLista()
print(c)