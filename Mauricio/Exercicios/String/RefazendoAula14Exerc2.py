#ler str e caractere. Qnt vezes o caractere aparece na str

palavra = input("Digite uma palavra: ")

caractere = input("Digite uma letra: ")

soma = 0
for i in range(len(palavra)):
    if caractere == palavra[i]:
        soma += 1

print(f"A quantidade de vezes que o caractere apareceu na palavra é igual a: {soma}")

print(palavra.count(caractere))