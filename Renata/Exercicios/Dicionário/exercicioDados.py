'''
Faça um programa em Python que simule uma jogada de um
dado 100 vezes e após imprima a ocorrência de cada
valor do dado.
'''
from random import randint

jogadas = []
for i in range(100):
    jogadas.append(randint(1,6))

d = {}
for valor in jogadas:
    d[valor] = d.get(valor,0) + 1

for valor in sorted(d):
    print (f"{valor}: {d[valor]}")
