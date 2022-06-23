#ler um e-mail e mostrar o domínio

email = input("Digite um e-mail: ")

arroba = email.find("@")
ponto = email.find(".")

dominio = ""

dominio += email[arroba+1:ponto]

print(f"Domínio: {dominio}")