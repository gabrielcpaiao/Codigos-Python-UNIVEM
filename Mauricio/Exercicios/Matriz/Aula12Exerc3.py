a = [0]*5
for i in range(5):
    a[i] = [0]*5
    for j in range(5):
        a[i][j] = int(input())
print(a)
for n in range (5):
    for m in range(5):
        if (n>m):
            print(a[n][m])
'''
for n in range(5):
    for m in range(1, 5):
    print(a[m][n]) 
'''