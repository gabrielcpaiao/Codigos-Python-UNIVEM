#Ciência da computação, UNIVEM 2021, 1º Ano e 2º Semestre (Programação de computadores)
#Avaliação final (Jogo da forca)
#Gabriel Costa Paião (RA:618764)
#Genésio Henrique da Silva (RA: 615539)
#Enrico Aparecido Ribeiro Pinarelli (RA: 615579)

from random import randint
arquivo = open("provaForca.txt", "r")

dicionario = {}
chaves = []

for line in arquivo:
    linha = line.split()
    chaves.append(linha[0])
    dicionario.setdefault(linha[0],linha[1])

sorteioChave = randint(0,len(chaves)-1)


tracinhos = ["-"]*len(chaves[sorteioChave])
traco = "".join(tracinhos)
print(traco)

palavraSorteada = chaves[sorteioChave].lower()
tentativa = 0
letrasDigitadas = []
erro = 0

resultado = 2


while True:
    print("Digite uma letra: ")
    letra = input()
    if letra in letrasDigitadas:
        print("Essa letra já foi digitada")
    else:
        if letra in palavraSorteada:
            posicao = 0
            for str in palavraSorteada:
                if str == letra:
                    tracinhos[posicao] = str
                    posicao += 1
                else:
                    posicao += 1
            traco = "".join(tracinhos)
            print(traco)
            tentativa += 1
        else:
            erro += 1
            print(f"Você já errou {erro} vez(es). Ainda pode errar {6-erro} vez(es)")
            print("Essa letra não está na palavra.")
            tentativa += 1
            traco = "".join(tracinhos)
            print(traco)
        letrasDigitadas.append(letra)
    if erro == 3:
        print(f"Vou te ajudar com uma dica: {dicionario[palavraSorteada]}")
    if erro == 6:
        print(f"Você perdeu. A palavra correta era '{palavraSorteada}'")
        resultado = 0
        break
    testando = 0
    for teste in palavraSorteada:
        if teste in letrasDigitadas:
            testando += 1
    if testando == len(palavraSorteada):
        print("Parabéns! Você acertou a palavra.")
        resultado = 1
        break