#Gabriel Costa Paião (RA:618764). Ciência da Computação. UNIVEM. 1º ano e 1º etapa, Noturno.
#Prova Final --> Exercício (1)
'''
Elabore um programa que leia um vetor de 20 notas reais. Em estatística, é muito
comum para o cálculo da média, desconsiderar a maior e a menor entre todas as
notas. Assim, faça um programa que calcule a média aritmética entre as 18 notas
restantes (não considerar a maior e nem a menor das notas).
'''
v = [0]*20
for i in range(20):
    v[i] = float(input(f"Digite a {i+1}º nota: "))
v.sort()
print()
print("Notas em ordem crescente: ")
print(v)
soma = 0
for i in range(1,19):
    soma += v[i]
print()
media = soma/18
print(f"A média entre as 18 notas restantes é: {media}")