print("Digite um número inteiro positivo: ")
while True:
    n = int(input())
    if n < 0:
        print("Número inválido. Digite um número inteiro e positivo.")
    else:
        break

numero = n

num_primo = 2
divisores = []
while n != 1:
    if n % num_primo == 0:
        n = n / num_primo
        divisores.append(num_primo)
    else:
        num_primo += 1

print(f"Para o número {numero}, sua fatoração é igual ao produto dos números: {divisores}")