#LIST COMPREHENSIONS  https://pythonhelp.wordpress.com/2011/03/01/list-comprehension/

import math

lista = input("Digite os números separados por espaço: ").split()
print(lista)
lista = [int(num) for num in lista]
print("Números digitados transformados em int: ",lista)

lista1 = [1, 4, 9, 16, 25]
lista2 = [math.sqrt(x) for x in lista1]
print("Lista 1 (Números de entrada): ",lista1)
print("Lista 2 (Raiz quadrada dos números): ",lista2)


S = [x*2 for x in range(10)]
print(S)

S = [x*2 for x in range(10) if x % 2 == 0]
print(S)

'''
#igual a
S = []
for x in range(10):
    if x % 2 == 0:
        S.append(x*2)
print(S)
'''

L = [[x,y] for x in range(5) for y in range(3)]
print(L)

print([s.capitalize() for s in ['um', 'dois', 'tres']])
print([[s.capitalize(), s.upper(), len(s)] for s in ['um', 'dois', 'tres']])

