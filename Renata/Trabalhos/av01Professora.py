'''
Elabore um programa em Python que leia uma string contendo um
nome completo e o converta para que todos os nomes da string
tenham a 1ª letra em maiúsculo e as demais em minúsculo, menos os
pronomes ‘da’, ‘de’, ‘dos’.
Imprima a nome convertido.

Exemplo:

Nome informado: joão da silva telles
Nome convertido: João da Silva Telles
'''

#1ª solução
pronomes = ["da", "dos", "do", "das", "e", "la", "de", "von"]
nomeInserido = input("Informe um nome >> ")
nomeAlterado = ""
nomeLista = nomeInserido.split()
for nome in nomeLista:
	nome = nome.lower()
	if nome not in pronomes:
		nome = nome.capitalize()
	nomeAlterado += nome +" "
print(nomeAlterado)

#2ª solução
pronomes = ["da", "dos", "do", "das", "e", "la", "de", "von"]
nomeInserido = input("Informe um nome >> ")
nomeLista = nomeInserido.lower().split()
for i, nome in enumerate(nomeLista):
	if nome not in pronomes:
		nomeLista[i] = nome.capitalize()
nomeAlterado = " ".join(nomeLista)
print(nomeAlterado)

#3ª solução
pronomes = ["da ", "dos ", "do ", "das ", "e ", "la ", "de ", "von "]
nomeInserido = input("Informe um nome >> ")
nomeAlterado = nomeInserido.title()
for pro in pronomes:
	nomeAlterado = nomeAlterado.replace(pro.capitalize(),pro.lower())
print(nomeAlterado)

#4ª solução
nome = input("Digite um nome: ").lower().split()
for i in range (len(nome)):
    if nome[i] not in ["da","de","do","das","dos"]:
        nome[i] = nome[i].capitalize()
nome = " ".join(nome)
print(nome)