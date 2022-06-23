#Cópia de lista

L = [1,2,3,4,5]
V = L #copia o endereço, então elas apontam para o mesmo lugar na memória
print("L ->",L)
print("V ->",V)
L[0] = 10
print("L ->",L)
print("V ->",V)

#Solução
L = [1,2,3,4,5]
V = L[:]  # copia o conteúdo de L para V, poderia ser V = L.copy()
print("L ->",L)
print("V ->",V)
L[0] = 10
print("L ->",L)
print("V ->",V)