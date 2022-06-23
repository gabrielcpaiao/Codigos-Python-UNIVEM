#Trabalho: Cifra de Transposição
#Gabriel Costa Paião (RA: 618764) Ciência da Computação. UNIVEM, 1º ano e 1º etapa.
#Validar a palavra chave sem letras repetidas.
#usar como frase: a pesquisa em uma tabela pode ser mais eficiente se os dados forem mantidos em ordem.
palavraChave = input("Digite a palavra chave: ").lower()
frase = input("Digite uma frase: ").lower()

qtdLinha = (len(frase)//len(palavraChave))
if len(frase)%len(palavraChave) != 0:
    qtdLinha += 1
m = [0]*qtdLinha
posicao = 0
x = len(palavraChave)

for i in range(qtdLinha):
    if posicao <= len(frase):
        m[i] = frase[posicao:x]
        posicao += len(palavraChave)
        x += len(palavraChave)
    else:
        break

'''if len(m[qtdLinha]) != len(palavraChave):
    m.insert(qtdLinha,"0"*(len(palavraChave)-len(m[qtdLinha])))'''

print(m)
#Não formou uma matriz completa (alguns elementos na última linha não conseguiram concluir o número total de colonas).

palavraChave = list(palavraChave)
copiaPalavraChave = palavraChave.copy()
copiaPalavraChave.sort()
print(copiaPalavraChave)
lista = []

for i in range(len(palavraChave)):
    for j in range(len(palavraChave)):
        if copiaPalavraChave[i] == palavraChave[j]:
            lista.append(j)

print(lista)


resposta = [0]*qtdLinha
for i in range(qtdLinha):
    resposta[i] = [0]*len(palavraChave)
    for j in range(len(palavraChave)):
        resposta[i][j] = m[j][lista[i]]

print(resposta)



#Daqui pra baixo não:
'''
resposta = [0]*qtdLinha

for i in range(len(palavraChave)):
    for j in range(qtdLinha):
        resposta

for i in range(qtdLinha):
    for j in range(len(palavraChave)):
        resposta.append(m[i][j])


print(resposta)



for caracter in frase:
    if len(linha) == len(palavraChave):
        matriz.append(linha.copy())
        linha.clear()
    else:
        linha.append(caracter)


for i in range(qtdLinha):
    if posicao <= len(frase):
        m[i] = frase[posicao:x]
        posicao += len(palavraChave)
        x += len(palavraChave)
    else:
        break
'''