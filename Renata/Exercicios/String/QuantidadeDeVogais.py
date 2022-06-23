frase = input("Digite uma frase: ")
vogal = ["a", "e", "i", "o", "u"]

soma = 0
for i in range(len(frase)):
    if frase[i] in vogal:
        soma += 1

print(f"O total de vogais digitadas na frase é: {soma}")

'''
Professora
#count() - conta as ocorrências

frase = "Hoje é terça-feira"
print(frase.count('a'))

#Faça um programa que mostre quantas vogais tem uma frase
#digitada pelo usuário
#1ª solução
cv = 0
for letra in frase.upper():
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        cv += 1
print(f"Tem {cv} vogais na frase")

#2ª solução
f = frase.upper()
cv = f.count('A') + f.count('E') + f.count('I') + f.count('O') + f.count('U')
print(f"Tem {cv} vogais na frase")

#3ª solução
cv = 0
vogais = 'AÁÃÂÀEÉIÍOÓÕÔUÚ'
for letra in frase.upper():
    if letra in vogais:
        cv += 1
print(f"Tem {cv} vogais na frase")

#4ª solução
cv = 0
vogais = 'AÁÃÂÀEÉIÍOÓÕÔUÚ'
for v in vogais:
    cv += frase.upper().count(v)
print(f"Tem {cv} vogais na frase")
'''