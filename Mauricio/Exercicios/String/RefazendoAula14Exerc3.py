#ler uma frase e ver e uma palavra existe na frase:
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")
L = frase.split(" ")
print(L)

if palavra in frase:
    print(f"A palavra ({palavra}) está contida na frase.")
else:
    print(f"A palavra ({palavra}) não está contida na frase!")