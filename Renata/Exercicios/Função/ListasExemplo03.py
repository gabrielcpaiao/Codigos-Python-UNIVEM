#Percorrendo uma lista
L = ["Ana", "Roberta", "Claudio", "Antônio", "Júlia"]

print("Percorrendo com while")
i = 0
while i < len(L):
    print(L[i])
    i += 1

print("Percorrendo com for in range")
for i in range(len(L)):
    print(L[i])

print("Percorrendo com for in")
for nome in L:
    print(nome)

print("Percorrendo com for in usando enumerate")
for i, nome in enumerate(L):
    print(i,nome)