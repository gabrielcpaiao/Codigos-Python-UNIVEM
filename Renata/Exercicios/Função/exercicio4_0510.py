'''
Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de
contadores(1-6) e uma função para gerar números aleatórios, simulando os
lançamentos dos dados.
'''

'''
from random import randint
lancamentos = []
for i in range(100):
    lancamentos.append(randint(1,6))

lancamentos.sort()
print(lancamentos)

dado = []
for i in range(1,7):
    dado.append(lancamentos.count(i))
    print(f"O número {i} saiu {dado[i-1]} vezes")
'''

from random import randint
def lançaDado():
    valores_lançamentos = [randint(1, 6) for i in range(100)]
    return valores_lançamentos

def contaValores(lista):
    for i in range(1, 7):
        print(f'o valor {i} foi sorteado {lista.count(i)}')

valores = lançaDado()
chama = contaValores(valores)
