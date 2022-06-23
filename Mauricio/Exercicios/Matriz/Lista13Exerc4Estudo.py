'''
Indicar a coordenada da peça
Movimentos da Rainha = 1
'''
m = [0]*8
for i in range(8):
    m[i] = [0]*8
print("Escreva a posição que a peça está.")
x = int(input("Valor do eixo X: "))
y = int(input("Valor do eixo Y: "))

for i in range(8):
    for j in range(8):
        if i + j  == (x-1) + (y-1) or (x-1) - (y-1) == i - j or i == (x-1) or j == (y-1):
            m[i][j] = 1
        print(f"{m[i][j]:^2}",end=" ")
    print()