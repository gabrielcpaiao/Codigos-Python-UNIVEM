m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        if i == j or i+j==4:
            m[i][j] = 1
        else:
            m[i][j] = 0
        print(f"{m[i][j]:^2}",end=" ")
    print()