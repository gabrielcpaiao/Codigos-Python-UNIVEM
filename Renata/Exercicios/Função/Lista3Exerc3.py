'''
Faça um programa em Python que implemente uma função INVERTE que receba um
número como parâmetro e retorne este número escrito ao contrário. Ex: 4312  2134. Peça
um número, chame a função e imprima o resultado.
'''
def inverteNum(n):
    print(n[-1::-1])

print("Digite um número: ")
num = input()
inverteNum(num)