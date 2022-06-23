'''
Indicar a coordenada da peça
Movimentos da torre = 1
'''
m = [0]*8
for i in range(8):
    m[i] = [0]*8
print("Escreva a posição da peça: ")
x = int(input("Valor do eixo X: "))
y = int(input("Valor do eixo Y: "))

for i in range(8):
    for j in range(8):
        if i == x or j == y:
            m[i][j] = 1
        print(f"{m[i][j]:^2}",end=" ")
    print()