'''
7
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''
frase = input("Digite uma frase: ").lower()
x = frase.count(" ")
vogais = ["a","e","i","o","u"]
soma = 0
for i in range(len(frase)):
    for j in range(len(vogais)):
        if vogais[j] == frase[i]:
            soma += 1
print(f"Há {x} espaços na frase escrita e apareceram {soma} vogais nela.")