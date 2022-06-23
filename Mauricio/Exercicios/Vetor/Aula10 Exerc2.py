a = []
b = []
for i in range(5):
    a.insert(i, int(input()))
for i in range(5):
    b.insert(i, int(input()))
c = []
for i in range(5):
    c.insert(i, (a[i])+(b[i]))
    print(f"{c[i]}")