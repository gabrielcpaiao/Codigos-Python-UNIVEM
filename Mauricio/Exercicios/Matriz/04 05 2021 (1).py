#matriz 5x5 e mostrar a diagonal secundária:
a = [0]*5
for i in range(5):
    a[i] = [0]*5
    for j in range(5):
        a[i][j] = int(input())
print(a)
print("Diagonal secundária:")
for n in range(5):
    for m in range(5):
        if (n+m==4):
            print(a[n][m])