'''
5. Faça um programa em Python que leia uma String e a escreva invertido.
'''

nome = input("Informe um nome >> ")
#1ª Solução
print(nome[::-1])

#2ª Solução
for i in range (len(nome)-1,-1,-1):
    print(nome[i],end="")
print()

#3ª Solução
inv = ""
for i in range (len(nome)-1,-1,-1):
    inv += nome[i]
print(inv)

#4ª Solução
inv = list(nome)
inv.reverse()
nome = "".join(inv)
print(nome)