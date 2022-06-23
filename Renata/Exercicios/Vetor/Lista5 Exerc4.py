from random import randint
l = []
v = []
x = int(input("Digite um valor: "))
for i in range(20):
    l.append(randint(1,50))
    if l[i] % x == 0:
        v.append(l[i])
print("O vetor gerado é: ")
print(l)
print(f"O vetor gerado dos números multiplos de {x} é:")
print(v)