#ler uma frase e criar sigla com as primeiras letras de cada frase.
frase = input("Digite uma frase: ")
L = frase.split(" ")
M = []
for i in range(len(L)):
    M.append(L[i][0])

print(M)
M = "".join(M)
print(M)