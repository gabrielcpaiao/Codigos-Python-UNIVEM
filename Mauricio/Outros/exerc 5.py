print("Digite o peso da pessoa: ")
peso = float(input())
print("Digite a altura da pessoa:")
altura = float(input())

imc = peso /(altura**2)
print("IMC = ", imc)
if (imc<18.5):
    print("Peso baixo!")
elif (imc <25):
    print("Peso normal!")
elif (imc<30):
    print("Sobrepeso")
elif imc<35:
    print("Obesidade grau I")
elif imc <40:
    print("Obresdade grau II")
else:
    print("Obesidade grau III")