#ler um str e um caractere. Qnt vezes o caractere aparece na str.
print("Digite uma palavra: ")
p = input()
print()
print("Digite um caractere: ")
c = input()
print()
print(p.count(c))
print()
soma = 0
for i in range(len(p)):
    if c == p[i]:
        soma += 1
print(soma)