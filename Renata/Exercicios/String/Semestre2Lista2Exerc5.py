'''
Elabore um programa em Python que lê uma String e calcule e imprima um código utilizando a
seguinte regra: para cada vogal, somar 5 pontos, para cada consoante somar 10 pontos,
desconsiderando qualquer outro caractere.
'''

caractere = input("Digite uma string: ").lower()

vogal = "aeiou"

soma5 = 0
soma10 = 0

for letra in caractere:
    if letra in vogal:
        soma5 += 5
    else:
        soma10 += 10


print(f"O código é: {soma10+soma5}")