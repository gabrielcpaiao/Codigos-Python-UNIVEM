#retirar de uma frase uma palavra existente
'''frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra a ser retirada da frase: ")

frase = frase.split(" ")

if palavra in frase:
    frase.remove(palavra)

frase = " ".join(frase)
print(frase)

email = input("Digite um e-mail: ")
x = email.find("@")
y = email.find(".com")
print("O domínio do e-mail é: ")
print(email[x+1:y])

nome = input("Digite um nome que servira como e-mail: ").lower()
nome = nome.split()
print(nome)
email = "@hotmail.com"
nome = "".join(nome)+email
print(nome)'''