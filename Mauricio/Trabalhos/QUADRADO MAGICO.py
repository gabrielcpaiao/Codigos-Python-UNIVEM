#Gabriel Costa Paião (RA: 61876-4). Ciência da Computação, 1 ano, 1 etapa.
print("Digite um valor (maior que dois) para o lado da matriz: ")
while True:
    l = int(input())
    if l <= 2:
        print("Valor inválido. Digite outro número.")
    else:
        break
S = (l + (l**3))/2
print(f"O valor do somatório das linhas, colunas e diagonais deverá ser igual a {S} para que a Matriz em questão seja considerada 'Quadrado mágico'.")
print()
m = [0]*l
for i in range(l):
    m[i] = [0]*l
    for j in range(l):
        m[i][j] = int(input(f"Digite o valor da posição M{i}x{j} desta matriz: "))
print()
print("Matriz gerada")
for i in range(l):
    for j in range(l):
        print(f"{m[i][j]:^5}", end=" ")
    print()

Resultado = []
diagonalPrin = 0
diagonalSec = 0
for i in range(l):
    somaLinhas = 0
    somaColunas = 0
    for j in range(l):
        somaLinhas += m[i][j]
        somaColunas += m[j][i]
        if i==j:
            diagonalPrin += m[i][j]
        if i+j == (l-1):
            diagonalSec += m[i][j]
    Resultado.append(somaLinhas)
    Resultado.append(somaColunas)
Resultado.append(diagonalPrin)
Resultado.append(diagonalSec)
print()
print("Estes são os valores da soma dos elementos das linhas, colunas e diagonais (Não nesta ordem): ")
print(Resultado)
print()
#Comparando todos os valores do vetor resultado (caso um seja diferente, a matriz não é quadrado mágico)
sim = True
for i in range(len(Resultado)):
    for j in range(len(Resultado)):
        if Resultado[i] != Resultado[j]:
            sim = False
            break
if sim:
    print("Esta matriz É uma matriz dita 'Quadrado mágico'.")
else:
    print("Esta matriz NÃO é dita 'Quadrado Mágico'.")