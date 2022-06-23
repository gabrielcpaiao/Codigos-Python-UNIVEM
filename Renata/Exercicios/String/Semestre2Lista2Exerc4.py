'''
Faça um programa em Python que leia uma lista de nomes e depois coloque-os em ordem
alfabética. Pode pedir a lista de nomes usando split() ou pedindo a quantidade de nomes antes do
laço, ou ainda, dentro do laço, perguntar a cada entrada se deseja entrar com mais um nome.
'''

lista = []

verificador = True
while verificador:
    print("Digite 1 para inserir um nome ou 2 para sair:")
    numero = input()
    if numero == "1":
        nome = input("Digite o nome: ").lower()
        lista.append(nome)
    elif numero == "2":
        break
    elif numero != "1" or numero != "2":
        print("Caractere inválido. Digite 1 ou 2.")
print()
lista.sort()
print(f"A lista de nomes em ordem alfabéticas fica:")
print(lista)