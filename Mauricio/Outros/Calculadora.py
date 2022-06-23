#Calculadora
print("Selecione uma das operações desejadas.")
print()
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print()
print("Digite sua opção: ")
while True:
    n = int(input())
    if 1 <= n <=4:
        break
    else:
        print("Opção inválida. Digite um número entre 1 e 4.")
x1 = int(input("Digite o primeiro número: "))
x2 = int(input("Digite o segundo número: "))
if n == 1:
    print(f"O resultado da operação escolhida (soma) é igual a: {x1+x2}")
elif n == 2:
    print(f"O resultado da operação escolhida (subtração) é igual a: {x1-x2}")
elif n == 3:
    print(f"O resultado da operação escolhida (Multiplicação) é igual a: {x1*x2}")
elif n == 4:
    print(f"O resultado da operação escolhida (Divisão) é igual a: {x1/x2}")