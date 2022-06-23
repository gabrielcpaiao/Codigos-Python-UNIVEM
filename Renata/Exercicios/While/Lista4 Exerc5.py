cont = 1
soma0 = 0
soma1 = 0
while(cont<=10):
    num = float(input("Digite um número: "))
    if (num%2==0):
        soma0 += num
        cont +=1
    else:
        soma1 += num
        cont += 1
print(f"A soma dos números pares é igual a {soma0} e a soma dos númerps ímpares é igual a {soma1}")