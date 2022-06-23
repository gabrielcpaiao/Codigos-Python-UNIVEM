distancia = float(input("Digite a distância percorrida pelo carro em KM: "))
gasolina = float(input("Digite o consumo do veículo em (L): "))
consumo = distancia/gasolina
if(consumo<8):
    print("Venda o carro")
elif (consumo<=14):
    print("Econômico")
else:
    print("Supereconomico")