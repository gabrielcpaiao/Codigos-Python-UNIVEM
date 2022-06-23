#Bubble sorte
v = [0]*5
print("Digite os valores do vetor desejado: ")
for i in range(5):
    v.insert(i, int(input()))
for i in range(5):
    for j in range(i+1, 5):
        if v[j] < v[i]:
            v[j], v[i] = v[i], v[j]
print(v)

#Select sort
v = [0]*5
print("Digite os valores do vetor desejado: ")
for i in range(5):
    v.insert(i, int(input()))
for i in range(5):
    menor = v[i]
    pos = i
    for j in range(i+1, 5):
        menor, pos = v[i], j
    v[pos] = v[i]
    v[i] = menor
print("Vetor ordenado: ", v)