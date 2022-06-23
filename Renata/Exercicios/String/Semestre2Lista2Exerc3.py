# Escreva um programa em Python que leia uma frase e informe a quantidade de palavras
#presentes na string.

frase = input("Digite uma frase:\n")

frase = frase.split()

print(f"Existe {len(frase)} palavras nesta frase!")