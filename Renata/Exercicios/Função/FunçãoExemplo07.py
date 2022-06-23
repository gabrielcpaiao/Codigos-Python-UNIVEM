from random import randint

def geraLista(L, tam, ini, fim):
    for i in range(tam):
        L.append(randint(ini,fim))

a = []
geraLista(a, 10, 1, 50)
print(a)

b = []
geraLista(b, 20, 1, 100)
print(b)

c = []
geraLista(c, 5, 10, 20)
print(c)