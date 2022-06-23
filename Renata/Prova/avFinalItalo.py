from random import randint
import unicodedata
arquivo = open("provaForca.txt", "r")

dicionario = {}
lista = []

for line in arquivo:
    (key, val) = line.split()
    key = unicodedata.normalize("NFKD", key.lower()).encode("ascii", "ignore").decode("utf-8")
    lista.append(key)
    dicionario[(key)] = val

item = lista[randint(0, len(dicionario) - 1)]
atual = ["_"] * len(item)
letras = []
erros = 0

while erros < 6 and "_" in atual:
    temp = "".join(atual)

    print(f"{temp}")

    if erros > 0:
        if erros != 1:
            print(f"Você ainda pode errar mais {6 - erros} vezes")
        else:
            print(f"Você ainda pode errar mais {6 - erros} vez")

    if erros >= 3:
        print(f"Dica: {dicionario[item]}")

    letra = unicodedata.normalize("NFKD", input("Letra: ")).encode("ascii", "ignore").decode("utf-8")

    if len(letra) != 1:
        print("Insira apenas uma letra")
        continue
    elif letra in letras:
        print("Letra já foi inserida antes")
        continue

    pos = 0
    erro = 1

    while pos != -1:
        pos = item.find(letra, pos)

        if pos != -1:
            atual[pos] = letra
            erro = 0
            pos += 1

    if erro:
        print("Letra não está na palavra")
        erros += 1
    else:
        print("Letra encontrada na palavra")

    letras.append(letra)

if erros >= 6:
    print(f"Você perdeu o jogo, a palavra era '{item}'")
else:
    print(f"Você ganhou o jogo, a palavra era '{item}'")