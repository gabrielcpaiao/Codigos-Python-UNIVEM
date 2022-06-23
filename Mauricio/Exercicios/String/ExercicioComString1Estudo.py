#ler duas strings mostre o conteudo e o tamanho
palavra1 = input("Digite uma palavra: ").lower()
palavra2 = input("Digite outra palavra: ").lower()
print(f"O tamanho da palavra {palavra1} é de {len(palavra1)} caracteres.")
print(f"O tamanho da palavra {palavra2} é de {len(palavra2)} caracteres.")
if len(palavra1) == len(palavra2):
    print("As duas palavras são do mesmo tamanho.")
else:
    print("As palavras possuem tamanhos diferentes.")
soma = 0
for i in range(len(palavra1)):
    if palavra1[i] == palavra2[i]:
        soma += 1

if soma == len(palavra1):
    print("As palavras possuem o mesmo conteúdo.")
else:
    print("As palavras possuem conteudos diferentes.")