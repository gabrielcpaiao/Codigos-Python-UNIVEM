'''
Faça um programa em Python que leia um nome e o escreva tantas vezes quantos forem seus
caracteres. Um nome por linha
'''
nome = input("Digite um nome: ")
for i in range(len(nome)):
    print(nome)
'''
print(f"{nome}\n"*len(nome)) 
'''