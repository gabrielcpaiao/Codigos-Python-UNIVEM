print("Digite um valor: ")
num = int(input())
cont = 1
soma = 0
while(cont <= num):
    soma += cont
    cont+=1
print("Soma final: ", soma)

#outro jeito
soma = 0
while (num > 0):
    soma += num
    num -= 1
print("Soma final: ", soma)