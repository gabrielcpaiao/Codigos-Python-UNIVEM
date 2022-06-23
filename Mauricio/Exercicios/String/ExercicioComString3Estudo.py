nome = input("Digite um nome: ")
for i in range(len(nome)):
    print(nome[:((len(nome)-i))])