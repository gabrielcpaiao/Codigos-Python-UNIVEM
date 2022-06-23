'''
 Implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo N.
Concatene não mais que N caracteres da string str2 a string str1.
'''

str1 = input("Digite uma string: ")

str2 = input("Digite uma string: ")

numero = int(input("Digite um número inteiro e positivo: "))

str1 += str2[:numero:1]

print(str1)

#print("".join([chr((ord(ch) - 64) % 26 + 65) for ch in input(">> ").upper()]))

'''
while True:
    palavra = input("Informe uma palavra apenas com letras de A a Z >> ").upper()
    if not palavra.isalpha():
        print("ERRO!! A palvra tem que conter apenas letras de A a Z")
    else:
        break
palCrip = ""
for letra in palavra:
    palCrip += chr(ord(letra)+1)
print(palCrip)
#Desafio, ficar somente entre as letras A e Z
palCrip = ""
for letra in palavra:
    palCrip += chr((ord(letra) - 64) % 26 + 65)
print(palCrip)
palCrip = ""
for letra in palavra:
    palCrip += chr(ord(letra) - (ord(letra)//90 * 26) + 1)
print(palCrip)
'''