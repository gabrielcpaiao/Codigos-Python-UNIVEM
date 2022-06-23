#MAP
import math
a, b = map(int,input("Digite dois números separados por espaço: ").split())
print(type(a),a)
print(type(b),b)

lista = list(map(int,input("Digite os números separados por espaço: ").split()))
print("Números digitados convertidos para inteiro: ",lista)

lista1 = [1, 4, 9, 16, 25]
lista2 = list(map(math.sqrt, lista1))
print("Lista 1 (Números de entrada): ",lista1)
print("Lista 2 (Raiz quadrada dos números): ",lista2)

#Faz a mesma coisa que o exemplo acima, utilizando for
'''
lista1 = [1,4,9,16,25]
lista2 = []
for num in lista1:
    lista2.append(math.sqrt(num))
print("Lista 1 (Números de entrada): ",lista1)
print("Lista 2 (Raiz quadrada dos números): ",lista2)
'''
#Faz a mesma coisa que o exemplo acima, utilizando Compreensão de Lista
'''
lista1 = [1,4,9,16,25]
lista2 = [math.sqrt(x) for x in lista1]
print("Lista 1 (Números de entrada): ",lista1)
print("Lista 2 (Raiz quadrada dos números): ",lista2)
'''

L1 = ['a','b','c']
L2 = list(map(str.upper,L1))
print("Lista 1 (Letras de entrada): ",L1)
print("Lista 2 (Letras em maiúsculo): ",L2)

def quad(x):
    return x**2
lista1 = list(range(1,11))
lista2 = list(map(quad,lista1))
lista3 = list(map(lambda x: x**2, lista1))
print("Lista 1 (Números de entrada): ",lista1)
print("Lista 2 (Números ao quadrado): ",lista2)
print("Lista 3 (Números ao quadrado) - usando lambda: ",lista2)

def potencia(x,y):
    return x**y
lista1 = list(range(1,6))
lista2 = [2,3,2,4,1]
lista3 = list(map(potencia,lista1,lista2))
print("Lista 1 (Bases): ",lista1)
print("Lista 2 (Expoentes): ",lista2)
print("Resultado: ",lista3)