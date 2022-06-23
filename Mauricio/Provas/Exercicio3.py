v = [0]*7

for i in range(7):
    v[i] = [0]*7


for m in range(7):
    for n in range(m+1):
        v[m][n] = m**2

for p in range(7):
    for q in range(p, -1, -1):
        v[q][p] = p**2

for a in range(7):
    for b in range(7):
        print(f"{v[a][b]:^3}", end=" ")
    print()