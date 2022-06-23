print("Informe a quantidade de:")
dias = int(input("Dias >> "))
horas = int(input("Horas >> "))
minutos = int(input("Minutos >> "))
segundos = int(input("Segundos >> "))

totalS = dias*24*60*60 + horas*60*60 + minutos*60 + segundos
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos é igual a {totalS} segundos")