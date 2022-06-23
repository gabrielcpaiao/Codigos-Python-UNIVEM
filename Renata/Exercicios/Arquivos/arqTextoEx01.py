nomeArq = input("Informe o nome do arquivo -> ")
try:
    nomeArq = "arquivos//"+nomeArq
    arquivo = open(nomeArq,"r")
except:
    print("Arquivo não exite")

import os

if os.path.exists("arquivos//texto.txt"):
    arquivo = open("arquivos//texto.txt", "r")
else:
    print("Arquivo não exite")
