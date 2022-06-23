palavra = input("Digite uma palavra: ")
if len(palavra)%2 !=0:
    print(palavra[len(palavra)//2])
else:
    print(palavra[(len(palavra) // 2)])
    print(palavra[(len(palavra) // 2) + 1])