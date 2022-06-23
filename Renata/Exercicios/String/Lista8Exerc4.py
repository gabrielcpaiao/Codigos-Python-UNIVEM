'''
Faça um programa em Python que leia uma String e dois caracteres. Troque todas as ocorrências
do primeiro caractere (podendo ser maiúsculo ou minúsculo) pelo segundo e imprima a
quantidade de vezes que o caractere foi substituído.
'''
'''
4. Faça um programa em Python que leia uma String e dois caracteres.
Troque todas as ocorrências do primeiro caractere (podendo ser maiúsculo ou minúsculo)
pelo segundo e imprima a quantidade de vezes que o caractere foi substituído.
'''

frase = input("Informe uma frase >> ").upper()
c1 = input("Informe a letra a ser substituída >> ").upper()[0]
c2 = input("Informe a letra para substituição >> ").upper()[0]

#1ª solução
qt = frase.count(c1)
frase = frase.replace(c1,c2)
print(f"Foram efetuadas {qt} substituições, frase alterada>> {frase}")

#2ª solução
qt = 0
L = list(frase)
for i in range(len(L)):
    if L[i] == c1:
        L[i] = c2
        qt += 1
frase = "".join(L)
print(f"Foram efetuadas {qt} substituições, frase alterada>> {frase}")