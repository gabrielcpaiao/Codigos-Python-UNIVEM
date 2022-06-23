palavra = input("Digite uma palavra: ").lower()
caractere = input("Digite um caractere: ").lower()
soma = 0
for i in range(len(palavra)):
    if caractere == palavra[i]:
        soma += 1
print(f"A quantidade de vezes que o caractere ({caractere}) apareceu na palavra foi: {soma} vezes.")