nome = input("Digite uma frase ou nome: ")
if nome == nome[::-1]:
    print("Este nome é palíndrome!")
else:
    print("Este nome não é palíndrome!")