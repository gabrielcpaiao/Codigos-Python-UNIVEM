massa = int(input("Digite a massa do material: "))
tempo = 50
massaF = massa/2
cont = 1
while (massaF >0.5):
    X = tempo//50
    massaF //= 2
    tempo += 50
print(f"A massa inicial era de {massa}g. A massa final é de {massaF}g. O tempo gasto nesta operação foi de {tempo} segundos")
