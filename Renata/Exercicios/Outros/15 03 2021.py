op = int(input("Digite (1) para calcular a area do retangulo. Digite (2) para calcular a area do triângulo: "))
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
if op!=1 and op!=2:
    print("Valor inválido")
elif op==1:
    area = base*altura
    print(area)
else:
    areaTriangulo = base*altura/2
    print(areaTriangulo)