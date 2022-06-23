#vogais representam mais de 50% dos caracteres. Ler uma risada e imprimir (muito ou pouco engraçado)
print("Digite uma forma de risada para ser analisada em muito ou pouco engraçado:")
risada = input().lower()
vogais = "aeiou"
print("A quantidade de vogais nesta risada é: ")
soma = 0
for i in range(len(vogais)):
    for j in range(len(risada)):
        if vogais[i] == risada[j]:
            soma += 1
print(soma)
print()
if soma > (len(risada))//2:
    print("Esta risada está com bastante intusiasmo.")
else:
    print("Esta está sem muito entusiasmo")

'''
print("Desafio 1 (Risadas)")
while True:
    inp = input(">> ").lower()
    cnt = [" " if c in "aeiou" else "" for c in inp].count(" ")
    print("Muito engraçada" if cnt > len(inp) // 2 else "Pouco engraçada")
    if input("Exit? ").lower()[0] in "ys":
        break
'''