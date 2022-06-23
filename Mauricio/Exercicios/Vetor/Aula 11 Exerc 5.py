a = []*10
b = []*10
c = []
print("Digite os valores do vetor A: ")
for i in range(10):
    a.insert(i, int(input()))
print("Digite os valores do vetor B: ")
for i in range (10):
    b.insert(i, int(input()))
for val in a:
    if val in b:
        c.append(val)
if len(c)>0:
    print("Intersecção: ", c)
else:
    print("Intersecção vazia!!")