#Gabriel Costa Paião (RA: 61876-4). UNIVEM-Noturno Ciência da Computação (1º ano, 1º etapa)
print("Digite a ordem da matriz que deseja: ")


while True:
    n = int(input())
    if n <= 1:
        print("Valor inválido. Digite um número maior que um (1).")
    else:
        break

m = [0]*n
for i in range(n):
    m[i] = [0]*n
    for j in range(n):
        if j == 0 or i == j:
            m[i][j] = 1

print()

for i in range(1,n):
    for j in range(1,n):
        m[i][j] = m[i-1][j-1] + m[i-1][j]
print("O Triângulo de Pascal formado é: ")
print()
for i in range(n):
    for j in range(n):
        print(f"{m[i][j]:^5}", end=" ")
    print()