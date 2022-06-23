m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        if i == j:
            m[i][j] = i**2
        else:
            m[i][j] = i*j
        print(f"{m[i][j]:^2}",end=" ")
    print()