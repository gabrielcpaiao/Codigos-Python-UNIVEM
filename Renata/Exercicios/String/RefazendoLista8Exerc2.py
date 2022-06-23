#ler uma frase e imprima qntas vogais tem a frase (maiúscula e minúscula).
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
soma = 0
for i in range(len(vogais)):
    for j in range(len(frase)):
        if vogais[i] == frase[j]:
            soma += 1
print(f"Esta frase tem {soma} vogais.")