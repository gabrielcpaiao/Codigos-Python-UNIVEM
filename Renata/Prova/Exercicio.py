#Peguei esse exercício com o Paulo

n = int(input("Digite o tamanho da matriz quadrada: "))
v = [0]*n

for i in range(n):
    v[i] = [0]*n
    for j in range(n):
        v[i][j] = int(input(f"Insira um valor para a posição {i},{j} da matriz: "))
print()
print("A matriz digitada é:")

for p in range(n):
    for q in range(n):
        print(f"{v[p][q]:^2}", end=" ")
    print()

resultado = []

for a in range(n):
    soma = 0
    for b in range(n):
        if v[b][a] == 0:
            soma += 1
    resultado.append(soma)

print(f"Há {resultado.count(n)} colunas nulas na matriz")