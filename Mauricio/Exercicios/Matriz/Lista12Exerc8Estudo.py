from random import randint
m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        if (i + j)%2 == 0:
            m[i][j] = 0
        else:
            m[i][j] = 1
        print(f"{m[i][j]:^2}",end=" ")
    print()