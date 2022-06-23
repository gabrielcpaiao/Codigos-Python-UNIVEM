#Trabalho 3. Gabriel Costa Paião   RA: 61876-4  (UNIVEM, Ciência da computação, 1º Ano, 1º Etapa)
A = []
B = []
C = []
for i in range(5):
    A.insert(i, int(input()))
for i in range(5):
    B.insert(i, int(input()))
print("O vetor A é igual a: ")
print(A)
print(" ")
print("O vetor B é igual a: ")
print(B)
sobe = 0
for n in range(4, -1, -1):
    if (A[n] + B[n] + sobe) >= 10:
        C.append((A[n] + B[n] + sobe) - 10)
        sobe = 1
        if (n==0):
            C.append(sobe)
    else:
        C.append(A[n] + B[n] + sobe)
        sobe = 0
print(" ")
print("O vetor resultante é: ")
C.reverse()
print(C)