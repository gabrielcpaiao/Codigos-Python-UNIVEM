'''
Faça um programa em Python para simular um
tradutor de palavras Português/Inglês – Inglês/Português.
Para isto crie um dicionário com duas palavras,
uma para armazenar a palavra em português e a
outra para o inglês. Faça um laço para armazenar N palavras,
informando as duas, após dê a opção ao usuário escolher
se ele quer entrar com uma palavra em inglês e
saber a tradução ou vice versa.
Faça uma busca da palavra informada e a
mostre na outra língua.
Permita quantas consultas o usuário desejar.
'''

def cadastrar():
    faixa("cadastro")
    while True:
        port = input("Palavra em português -> ").upper()
        ingl = input("Palavra em inglês -> ").upper()
        tradutor[port] = ingl
        resp = input("Inserir mais 1 palavra? [S/N] -> ").upper()[0]
        if resp != 'S':
            break

def listagem():
    faixa("listagem")
    for p, i in tradutor.items():
        print(f"Português: {p} - Inglês: {i}")

def portToIngles():
    port = input("Palavra em português -> ").upper()
    if port in tradutor:
        print(f"Tradução para o inglês -> {tradutor[port]}")
    else:
        print(f"'{port}' não consta no dicionário")

def inglesToPort():
    ingl = input("Palavra em inglês -> ").upper()
    if ingl in tradutor.values():
        indice = list(tradutor.values()).index(ingl)
        port = list(tradutor.keys())[indice]
        print(f"Tradução para o português -> {port}")
    else:
        print(f"'{ingl}' não consta no dicionário")

def faixa(texto):
    print("=" * 50)
    print(f"{' '.join(texto.upper())}".center(50))
    print("=" * 50)

tradutor = {}
cadastrar()
listagem()
while True:
    faixa ("Tradutor")
    op = int(input("1. Português para Inglês"
                   "\n2. Inglês para Português"
                   "\n3. Encerrar"
                   "\nOpção -> "))
    if op == 3:
        break
    elif op == 1:
        portToIngles()
    elif op == 2:
        inglesToPort()
    else:
        print("Opção inválida!!")
