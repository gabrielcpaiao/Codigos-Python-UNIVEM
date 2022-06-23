print("Digite uma frase qualquer: ")
f = input()
print()
f = f.split(" ")
sigla = ""
for i in range(len(f)):
    sigla += f[i][0]
print(f"As siglas das palavras é igual a: {sigla}")

'''
frase = input('Digite uma frase:\n>> ')
L = frase.split()
sigla = ""
for i in range(len(L)):
    sigla += L[i][0]
print(f'As primeiras letras de cada palavra foram: \"{sigla}\"')
'''