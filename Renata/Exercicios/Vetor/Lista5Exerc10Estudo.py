'''
 Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e peça
um número ao usuário. Verifique se este número pertence ou não ao vetor. Imprima
o vetor e a mensagem de número encontrado ou não
'''
from random import randint
a = []
for i in range(10):
    a.append(randint(1,50))
print(a)
num = int(input("Digite um número: "))
if num in a:
    print("Este número está no vetor!")
    print(a)
else:
    print("Este número não está no vetor!")
    print(a)