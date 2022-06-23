#le uma frase e retirar da frase uma palavra
print("Digite uma frase qualquer: ")
f = input()
print()
f = f.split(" ")
print("Digite uma palavra que deseja retirar da frase: ")
p = input()
print()
novafrase = ""
for i in range(len(f)):
    if p != f[i]:
        novafrase += f[i]
        novafrase += " "
print(f"A nova frase é: {novafrase}", end=" ")