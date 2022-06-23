'''
Indicar a coordenada da peça
Movimentos da cavalo = 1
'''
m = [0]*8
for i in range(8):
    m[i] = [0]*8
print("Escreva a posição que a peça está.")
x = int(input("Valor do eixo X: "))
y = int(input("Valor do eixo Y: "))

x -= 1
y -= 1

for i in range(8):
    for j in range(8):
        if i == x-1 and j == y-2 or i == x-2 and j == y-1 or i == x-1 and j == y+2 or i == x-2 and j == y+1 or i == x+1 and j == y-2 or i == x+2 and j == y-1 or i == x+2 and j == y+1 or i == x+1 and j == y+2:
            m[i][j] = 1
        print(f"{m[i][j]:^2}",end=" ")
    print()