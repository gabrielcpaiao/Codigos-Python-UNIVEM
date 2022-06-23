def numPrimo(num):
    if -1 <= num <= 1:
        return False
    for i in range (2,num//2 + 1):
        if num % i == 0:
            return False
    return True

def proximoPrimo():
    global primo
    while True:
        primo += 1
        if numPrimo(primo):
            break

def mmc(numeros):
    mmc = 1
    fimMmc = 0
    while fimMmc < totalNumeros:
        dividiu = False
        while dividiu == False:
            for j in range (totalNumeros):
                if numeros[j] == 1:
                    continue
                if numeros[j] == primo:
                    fimMmc += 1
                if numeros[j] % primo == 0:
                    dividiu = True
                    numeros[j] = numeros[j]//primo
            if dividiu:
                mmc *= primo
            else:
                proximoPrimo()


numeros = []
primo = 2
totalNumeros = int(input("Digite quantos numeros serao utilizados para o calculo do mmc: "))
for i in range (totalNumeros):
    numeros.append(int(input(f"Digite o {i + 1}º numero: ")))
mmc(numeros)
print(mmc)