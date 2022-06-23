num = []
maior = 0
menor = 1000
for i in range(5):
    num.insert(i, float(input()))
    if (num[i]>maior):
        maior = num[i]
    if (num[i]<menor):
        menor = num[i]
print(f"O maior valor é: {maior} e o menor valor é: {menor}")