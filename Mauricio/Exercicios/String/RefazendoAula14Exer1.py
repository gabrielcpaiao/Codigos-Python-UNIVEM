#ler uma str e ver se é palíndromo
nome = input("Digite uma palavra: ")

inv = nome[::-1]

if nome == inv:
    print("Palavra palíndromo!")
else:
    print("Palavra não palíndromo!")