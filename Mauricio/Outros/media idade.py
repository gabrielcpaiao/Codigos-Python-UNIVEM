soma = 0
cont = 0
while True:
    id = int(input("Digite uma idade: "))
    soma += id
    cont +=1
    media = soma / cont
    print(f"A média das idades é: {media}")
    if (id == 0):
        print("Idade inválida!!")
        break