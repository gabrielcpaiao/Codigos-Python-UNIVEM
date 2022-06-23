from random import randint
l = []
for i in range(10):
    l.append(randint(1,50))
print(l)
opc = int(input("Digite 1 para gerar o vetor na ordem direta ou 2 para ordem inversa: "))
if opc == 1:
    print(l)
else:
    l.reverse()
print(l)