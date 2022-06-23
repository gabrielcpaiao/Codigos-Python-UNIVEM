from random import randint
m = [0]*4
mes = []
somaTotal = 0
maior = 0
for i in range(4):
    m[i] = [0]*12
    for j in range(12):
        m[i][j] = randint(20,50)
        somaTotal += m[i][j]
        print(f"{m[i][j]:^2}",end=" ")
        if m[i][j] > maior:
            maior = m[i][j]
            semana = i
            ms = j
    print()
for i in range(12):
    mes.append((m[0][i]) + (m[1][i]) + (m[2][i]) + (m[3][i]))
print()
print(f"O total de peças produzidas em cada mês foi: ")
print(mes)
print()
print(f"O total de peças produzidas no ano foi: ")
print(somaTotal)
print()
print(f"A {semana+1}º semana do {ms+1} mês foi a que produziu maior quantidade de peças.")