#bruno.santos@univem.edu.br
#Ciência da computação 1º ano, 1º etapa (Noturno)
#Gabriel Costa Paião  (RA: 61876-4)
#Genésio Henrique (Ra: 615536)
#Enrico Pinarelli (RA: 615579)
a = []
b = []
for i in range(3):
    print(f"Insira o {i + 1}º elemento do conjunto A: ")
    a.insert(i, int(input()))
print("O conjunto A é igual a: {", *a,"}")
for i in range(4):
    print(f"Insira o {i + 1}º elemento do conjunto B: ")
    b.insert(i, input())
print("O conjunto B é igual a: {", *b,"}")
print("A matriz AxB")
for i in range (len(a)):
    for j in range(len(b)):
        print(f"({a[i]},{b[j]})", end=" ")
    print(" ")
print(" ")
print("A matriz BxA")
for i in range (len(b)):
    for j in range(len(a)):
        print(f"({b[i]},{a[j]})", end=" ")
    print(" ")
print(" ")
print(f"A quantidade de pares AxA é igual a: {len(a)*len(a)}")
print(f"A quantidade de pares AxB é igual a: {len(a)*len(b)}")
print(f"A quantidade de pares BxA é igual a: {len(b)*len(a)}")