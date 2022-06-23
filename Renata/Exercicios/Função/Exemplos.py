#Parâmetros
def calcMedia():
    a = int(input("Valor 1 >> "))
    b = int(input("Valor 2 >> "))
    media = (a + b) / 2
    print(f"A média é {media}")
def calcMed(a, b):
    media = (a + b) / 2
    print(f"A média é {media}")
calcMedia()
calcMed(8, 14)
x = 18
y = 10
calcMed(x, y)
calcMed(x, 20)
n1 = float(input("Nota 1 >> "))
n2 = float(input("Nota 2 >> "))
calcMed(n1, n2)

#Parâmetros e retorno
def calcMed(a, b):
    media = (a + b) / 2
    return media
nota1 = float(input("Nota 1 >> "))
nota2 = float(input("Nota 2 >> "))
m = calcMed(nota1, nota2)
if m >= 6:
    print(f"Aprovado com a média {m}")
else:
    print(f"Reprovado com a média {m}")

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

def validaNum(n):
    if n > 999:
        return False
    return True
num = int(input("Número >> "))
if validaNum(num):
    c = num // 100
    d = num % 100 // 10
    u = num % 10
    print(c, d, u)
else:
    print("Número inválido!!")