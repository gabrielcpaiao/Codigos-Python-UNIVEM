a = []
b = []
for i in range(10):
    a.append(i)
for i in range(10):
    b.append(i)
c = []
for i in range(10):
    c.append((a[i])*(b[i]))
    print(c)