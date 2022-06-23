#Faça um programa que gere um número aleatório (entre 1 e 10) e peça ao usuário para tentar adivinhar qual é o número, ou seja, peça um número ao usuário (entre 1 e 10). Imprima o número digitado, o número sorteado e se acertou ou não.
#Pesquisar método para gerar um número aleatório.
#As funções randrange() e randint() geram aleatoriamente um número inteiro dentro de um intervalo dado pelo usuário
print("Digite um número entre 0 e 10")
num = float(input())
import random
if num<0 or num>10:
    print("Número inválido")
elif num==x:
    x = random.randint(0, 10)
    print("O número escolhido é igual ao sorteado")
else:
    x = random.randint(0, 10)
    print("O número escolhido é diferente do sorteado")

#professora:
n = int(input("Qual número entre 1 e 10 você quer apostar? -> "))
if n not in range(1,11):
    print("O número apostado deveria estar entre 1 e 10")
else:
    ns = randint(1, 10)
    print(f"Número apostado = {n}\nNúmero sorteado = {ns}")
    if n == ns:
        print("VOCÊ GANHOU!! ACERTOU O NÚMERO")
    else:
        print("VOCÊ PERDEU!! NÃO ACERTOU O NÚMERO")
