x = []
y = []
for i in range(5):
    x.insert(i, int(input(f"Digite o {i+1}º valor do vetor X: ")))
    y.insert(i, int(input(f"Digite o {i+1}º valor do vetor Y: ")))
soma = []
for i in range(5):
    soma.insert(i, x[i]+y[i])
print(soma)
produto = []
for i in range(5):
    produto.insert(i, x[i]*y[i])
print(produto)
diferenca = []
for i in range(5):
    if x[i] not in y:
        diferenca.append(x[i])
print(diferenca)
interseccao = []
for i in range(5):
    for j in range(5):
        if x[i]==y[j]:
            interseccao.append(x[i])
print(interseccao)
for i in range(5):
    for j in range(5):
        if x[i]!=y[j]:
            x.append(y[j])
print(x)
'''
x = []
y = []


print("Informe 5 números da lista x")
while len(x) != 5:
    n = int(input("Número >> "))
    if n in x:
        print("Número repetido, digite novamente...")
    else:
        x.append(n)

print("=" * 50)

print("Informe 5 números da lista y")
while len(y) != 5:
    n = int(input("Número >> "))
    if n in y:
        print("Número repetido, digite novamente...")
    else:
        y.append(n)

print("=" * 50)
print("Lista x >>",x)
print("Lista y >>",y)
print("=" * 50)

soma = []
prod = []
dif = []
inter = []
uniao = x[:]

for i in range(5):
    soma.append(x[i] + y[i])
    prod.append(x[i] * y[i])
    if x[i] not in y:
        dif.append(x[i])
    else:
        inter.append(x[i])
    if y[i] not in uniao:
        uniao.append(y[i])

print("Soma            >>",soma)
print("Produto         >>",prod)
print("Diferença (x-y) >>",dif)
print("Intersecção     >>",inter)
print("União           >>",uniao)
'''