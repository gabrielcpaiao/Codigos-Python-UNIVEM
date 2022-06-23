vet = [0]*20
for i in range(20):
    vet[i] = int(input())
for i in range(10):
    vet[i], vet[i+10] = vet[i+10], vet[i]
print(vet)