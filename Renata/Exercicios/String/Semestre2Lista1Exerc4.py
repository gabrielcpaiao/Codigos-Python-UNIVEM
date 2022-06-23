'''
Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra.
Imprima a string resultante.

'''

palavra = input("Digite uma palavra: ")
print(palavra)
vetor = ""
for i in range(len(palavra)):
    vetor += (chr(ord(palavra[i]) + 1))

print(vetor)