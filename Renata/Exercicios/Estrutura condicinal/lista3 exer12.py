valor_desejado = float(input("Digite o valor a ser retirado: "))
n50 = valor_desejado//50
n10 = (valor_desejado%50)//10
n5 = ((valor_desejado%50)%10)//5
n1 = valor_desejado%5
print(f"Para este valor, o cliente irá retirar {n50} notas de B$50, {n10} notas de B$10, {n5} notas de B$5 e {n1} notas de B$1")