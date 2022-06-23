'''
Faça um programa em Python que peça
um número (n) ao usuário e armazene em um vetor de
10 posições de inteiros, a partir do número 1,
somando a cada número o valor de n.
Exemplo:
n=3
Vetor: 1 – 4 – 7 – 10 – 13 – 16 – 19 – 22 – 25 – 28
'''

n = int(input("Digite um número: "))
vetor = []
cont = 1
soma = 1
while cont <= 10:
    vetor.append(soma)
    soma += n
    cont += 1

print(vetor)