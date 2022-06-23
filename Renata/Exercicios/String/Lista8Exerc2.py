'''
Faça um programa em Python que leia uma frase e imprima quantas vogais tem esta frase.
Considerar minúscula e maiúscula.
'''
frase = input("Digite uma frase: ").lower()
vog = []
for i in range(len(frase)):
    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        vog.append(frase[i])
if vog == 0:
    print("Não há vogais nesta frase!")
else:
    print(f"Há {len(vog)} nesta frase.")