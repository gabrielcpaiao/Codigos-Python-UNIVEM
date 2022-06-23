palavra = input("Digite uma palavra: ")
if palavra[:] == palavra[::-1]:
    print("Palavra palindromo!")
else:
    print("Palavra não palíndromo.")