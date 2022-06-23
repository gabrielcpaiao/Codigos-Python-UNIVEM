from random import randint
l = []
par = 0
for i in range(20):
    l.append(randint(1,50))
    if l[i] % 2 == 0:
        par += l[i]/i
print("O vetor gerado é: ")
print(l)
print(f"A média dos valores pares deste vetor é igual a: {par} ")