n = float(input("Digite o valor do troco: "))
n *= 100
moedas = [100,50,25,10,5,1]
total = 0
v = [0]*6
for i in range(len(moedas)):
    num_moedas = n//moedas[i]
    v[i] = num_moedas
    n -= num_moedas * moedas[i]
    total += num_moedas
print()
print("Total de moedas:", total)
print()
for i in range(len(v)):
    print(f"Foram utilizadas {v[i]} de {moedas[i]} centavos.")
    print()
#Mostrar o total de cada moeda no troco