'''
 Ler uma frase e contar quantos caracteres são espaços em brancos.
'''

frase = input("Digite uma frase: ")

quantidade_de_espaco = frase.count(" ")

split = frase.split()

print(quantidade_de_espaco)
print(len(split))