'''Elabore um programa em Python que lê uma String e calcule e imprima um código utilizando a seguinte regra:
para cada vogal, somar 5 pontos, para cada consoante somar 10 pontos, desconsiderando qualquer outro caractere.
Exemplo: Linguagem de Programação

10 vogais (lembre-se de considerar vogais acentuadas) à 10 x 5 = 50

12 consoantes à 12 x 10 = 120
Código = 170'''

frase = input("Digite um nome ou frase: ").upper()

vogal = "AEIOUÀÁÉÍÓÚÃÕÂÊÎÔÛ"

SomaVog = 0
SomaCon = 0
'''for i in range(len(frase)):
    if frase[i] in vogal:
        SomaVog += 1
    else:
        SomaCon += 1

print(f"Pontos pelas vogais: {SomaVog*5}")
print(f"Pontos pelas consoantes: {SomaCon*10}")
print("Pontos totais: ",SomaVog*5 + SomaCon*10)
'''
#usando isalpha só seleciona as letras e não pega os espaços
for letra in frase:
    if letra.isalpha():
        if frase in vogal:
            SomaVog += 5
        else:
            SomaCon += 10
print(f"Pontos pelas vogais: {SomaVog}")
print(f"Pontos pelas consoantes: {SomaCon}")
print("Pontos totais: ",SomaVog + SomaCon)