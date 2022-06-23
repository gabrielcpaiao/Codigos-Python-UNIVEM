#ler um nome e gerar um e-mail (@univem.edu.br)

nome = input("Digite um nome: ").lower()
nome = nome.split()

email = "@univem.edu.br"

nomeCOMemail = "".join(nome)+email

print(f"O e-mail gerado é: {nomeCOMemail}")