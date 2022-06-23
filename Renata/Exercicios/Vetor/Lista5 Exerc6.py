from random import randint
A = []
for i in range(10):
    A.append(randint(1,50))
print(A)
x = int(input("Digite 1 para gerar o vetor na ordem direta ou 2 para ordem inversa: "))
B = []
for i in range(10):
    B.append(A[i]*x)
print(B)