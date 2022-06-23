'''
Faça um programa que receba do usuário um arquivo,
e mostre na tela quantas linhas esse arquivo possui.
'''

while True:
    filename = input("Entre com o nome do arquivo -> ")
    try:
        fp = open(filename,'r')
        linhas = fp.readlines()
        print(linhas)
        print(f"O arquivo tem {len(linhas)} linhas")
        fp.close()
        break
    except FileNotFoundError:
          print("Arquivo não existe")