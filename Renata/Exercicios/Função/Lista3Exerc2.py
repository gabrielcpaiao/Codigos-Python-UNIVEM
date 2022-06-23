'''
Escreva um programa em Python que implemente uma função potência, que receba uma
base e um expoente por parâmetro e retorne o valor da base elevada ao expoente. O expoente é
sempre maior ou igual a zero, e os números são sempre inteiros. Peça uma base e um expoente,
chame a função e imprima o resultado.
'''
def  potenciacao(base,expoente):
    resultado = 1
    for i in range(expoente):
        resultado *= base
    print(resultado)
print("Digite uma base: ")
n1 = int(input())
print("Digite um expoente: ")
while True:
    n2 = int(input())
    if n2 < 0:
        print("O expoente deve ser maior ou igual a zero.")
    else:
        break
print()
potenciacao(n1, n2)
