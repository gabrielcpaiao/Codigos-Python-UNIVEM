print("Digite um valor para servir como lado do triângulo: ")
a = float(input())
print("Digite um valor para servir como lado do triângulo: ")
b = float(input())
print("Digite um valor para servir como lado do triângulo: ")
c = float(input())

if ((a>b+c) or (b>a+c) or (c>b+a)):
    print("Algum valor escolhido não satisfaz a condição de existencia de um triângulo")
elif (a==b==c):
    print("Triângulo equilátero")
elif (a==b or b==c or a==c):
    print("Triângulo isóceles")
else:
    print("Triângulo escaleno")
