#ler dois numeros e transforma-los em binários. depois disso contar a quantidade em um (1) entre estes dois numeros
#bin(num) transforma em binário
print("Digite o primeiro número: ")
n1 = int(input())

print("Digite o segundo número: ")
n2 = int(input())

aux = ""
for i in range(n1,n2+1):
    a = bin(i)
    aux += a
print()
print(aux.count("1"))
'''cont = 0
for j in range(len(aux)):
    if aux[j] == "1":
        cont += 1 
print(cont)'''