#ler uma frase e uma palavra e ve se existe
print("Digite uma frase qualquer: ")
f = input()
print()
print("Digite uma palavra: ")
p = input()
print()
f = f.split(" ")
v = False
for i in range(len(f)):
    if p == f[i]:
        v = True
print()
if v:
    print("A palavra digitada está contida na frase escrita!")
else:
    print("A palavra digitada não está contida na frase escrita!")