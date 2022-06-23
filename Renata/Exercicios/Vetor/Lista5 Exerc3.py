from random import randint
l = []
mult = []
for i in range(20):
    l.append(randint(1,50))
    if l[i] % 5 == 0:
        mult.append(l[i])
print("O vetor gerado é: ")
print(l)
print("O vetor gerado dos números multiplos de 5 é:")
print(mult)