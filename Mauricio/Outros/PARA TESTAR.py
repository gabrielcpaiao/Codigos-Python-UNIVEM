'''print("Digite uma frase: ")
frase = input().lower()
print("Digite uma palavra para retirar da frase: ")
palavra = input().lower()
x = (frase.find(palavra))
print(x)
y = len(palavra)
fraseNova = frase[:8] + frase[8+y:]
print(fraseNova)'''

'''
palavraChave = input("Digite a palavra chave: ").lower()
palavraChave = palavraChave.split()
frase = input("Digite uma frase: ").lower()
print(palavraChave)
print(len(frase))

qtdLinha = (len(frase)//len(palavraChave))
if len(frase)%len(palavraChave) != 0:
    qtdLinha += 1

m = [0]*qtdLinha
posicao = 0
tamanho = True
for i in range(qtdLinha):
    m[i] = [0]*len(palavraChave)
    for j in range(len(palavraChave)):
        if posicao <= len(frase):
            m[i][j] =frase[posicao]
            posicao += 1
            tamanho = False
        else:
            break
    if not tamanho:
        break

for i in range(qtdLinha):
    for j in range(len(palavraChave)):
        print(f"{m[i][j]:^2}", end=" ")
    print()'''

num = int(input("Digite um número: "))

fator = []

while num > 1:
    for number in range(2, num + 1):
        if num % number == 0:
            fator.append(number)
            num = num // number
            break

print(fator)