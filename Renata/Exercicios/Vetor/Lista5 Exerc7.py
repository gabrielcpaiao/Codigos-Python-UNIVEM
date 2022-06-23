from random import randint
A = []
for i in range(10):
    A.append(randint(1,50))
print(A)
print("O vetor de forma ordenada fica:")
A.sort()
print(A)