'''
 O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de
substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto
abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria
substituído por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente um programa que faça
uso desse Código de César (3 posições), entre com uma string e retorne a string codificada.
Exemplo:
String: a ligeira raposa marrom saltou sobre o cachorro cansado
Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
'''

frase = input("Digite uma frase: ")
print(f"A frase digitada é: {frase}")

vetor = ""

for i in range(len(frase)):
    if frase[i] == "x":
        vetor += "a"
    elif frase[i] == "y":
        vetor += "b"
    elif frase[i] == "z":
        vetor += "c"
    else:
        vetor += chr(ord(frase[i]) + 3)

print(f"A frase codificada é: {vetor}")

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