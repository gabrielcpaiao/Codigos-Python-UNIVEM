'''
Faça um programa em Python que gere uma lista com 10 números aleatórios entre 1 e 50,
usando list comprehensions.
'''

from random import randint

L = [randint(1,50) for x in range(10)]
print(L)