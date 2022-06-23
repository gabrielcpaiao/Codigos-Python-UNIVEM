#Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
# com exceção ao dele próprio. Ex: a soma dos divisores do número
# 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

num = int(input("Digite um número inteiro: "))
cont = 0
for i in range(1, (num//2)+1):
    if num%i==0:
        print(i)
        cont += i
print(f"O valor final é igual a {cont}")