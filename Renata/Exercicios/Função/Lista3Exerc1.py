'''
Escreva um programa em Python que contenha uma função que peça um número e
verifique se é par ou ímpar. No principal, chame a função.
'''
def verificaNum(n):
    if n % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")
print("Digite um número: ")
n1 = int(input())
verificaNum(n1)
'''
def par_impar(a):
    if a % 2 == 0:
        return "par"
    return "imapar"
a = int(input('numero:'))
print(par_impar(a))
'''