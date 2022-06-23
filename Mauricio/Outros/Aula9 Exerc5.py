nota = 0
for i in range(3):
    nome = input()
    med = float(input())
    if (med> nota):
        nota = med
        nome1 = nome
print(f"O aluno {nome1} tirou a maior média. Esta média é de {nota}")

#Aluno
q = 0
r = 0
for i in range(3):
    x = input("Digite a média e o seu nome: ")
    m, n = x.split()
    m = float(m)
    n = str(n)
    if m > q:
        q = m
        r = n
print(f"maior média {q} e o aluno(a) {r}")