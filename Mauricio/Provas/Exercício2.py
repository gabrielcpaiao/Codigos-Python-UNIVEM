vetor = []

for i in range(20):
    x = int(input(f"Digite o {i+1}º número: \n"))
    vetor.append(x)

cont = 0
soma = 0
for n in range(19, 9, -1):
    if vetor[n] == vetor[cont]:
        soma += 1
        cont += 1

print(vetor)
if soma == 10:
    print("Este vetor é simétrico.")
else:
    print("Este vetor não é simétrico!")