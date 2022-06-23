a = []*5
b = []*5
c = []
print("Digite os valores do vetor A: ")
for i in range(5):
    a.insert(i, int(input()))
print("Digite os valores do vetor B: ")
for i in range (5):
    b.insert(i, int(input()))
c[0:5] = a[0:5]
for val in b:
    if val not in a:
        c.append(val)
print(c)