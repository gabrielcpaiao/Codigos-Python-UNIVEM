#Trabalho Bruno. Triangulazação de Gauss. UNIVEM Ciência da Computação (1º ano 2º etapa)
#Gabriel Costa Paião.     RA: 618764
#Vinicius Gomes Prieto.   RA: 615791
#Genésio Henrique da Silva RA: 615536
#Enrico  Pinarelli         RA:615579


m = [0] * 3
v = [0] * 4
n = [0] * 4
for i in range(3):
    m[i] = [0] * 4
    for j in range(4):
        m[i][j] = int(input(f"Digite o valor para a posição {[i]}{[j]} da matriz: "))
    print("=" * 100)

print()
print("=" * 100)
print("A matriz gerada é: ")
for i in range(3):
    for j in range(4):
        print(f"{m[i][j]:^2}", end=" ")
    print()

for j in range(4):
    v[j] = ((m[2][0] / m[0][0]) * m[0][j]) - (m[2][j])

for j in range(4):
    m[2][j] = v[j]

print()
print("=" * 100)
print("A matriz com a equação III modificada: ")
for i in range(3):
    for j in range(4):
        print(f"{m[i][j]:^5}", end=" ")
    print()

for j in range(4):
    v[j] = ((m[1][0] / m[0][0]) * m[0][j]) - (m[1][j])

for j in range(4):
    m[1][j] = v[j]

print()
print("=" * 100)
print("A matriz com as equações III e II modificada: ")
for i in range(3):
    for j in range(4):
        print(f"{m[i][j]:^5}", end=" ")
    print()

for j in range(1, 4):
    n[j] = ((m[2][1] / m[1][1]) * m[1][j]) - (m[2][j])

for j in range(1, 4):
    m[2][j] = n[j]
    if m[2][j] <= 10**-15:
        m[2][j] = 0

print()
print("=" * 100)
print("A matriz final: ")
for i in range(3):
    for j in range(4):
        print(f"{m[i][j]:^5}", end=" ")
    print()

print()
print("=" * 100)
x3 = m[2][3] / m[2][2]
x2 = (m[1][3] - m[1][2] * x3) / m[1][1]
x1 = (m[0][3] - m[0][2] * x3 - m[0][1] * x2) / m[0][0]
print(f"Os valores de x1, x2 e x3 são, respectivamente: {x1}, {x2} e {x3}")