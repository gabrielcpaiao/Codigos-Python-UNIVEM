'''
Faça um programa em Python que imprima todos os números primos de um intervalo
informado pelo usuário. Utilize o método do exercício 4 para verificar se o número é primo ou
não.
'''

def numPrimo():
    inicio = int(input("Digite o início do intervalo: "))
    fim = int(input("Digite o final do intervalo: "))
    numPrimos = []
    for i in range(inicio, fim+1):
        validacao = True
        for j in range(2, ((i) // 2) + 1):
            if i % j == 0:
                validacao = False
        if validacao:
            numPrimos.append(i)
    return print(f"Os números primos entre {inicio} e {fim} são: {numPrimos}")

numPrimo()