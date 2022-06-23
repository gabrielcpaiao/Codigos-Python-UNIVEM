#Ler altura e sexo. Calcular e imprimir o peso ideal
altura = float(input("Digite o valor da altura a ser calcula: "))
sexo = input("Digite o sexo: ")
if sexo== "m" or sexo=="M":
    print("O valor do peso ideal para tal opção é: ", (72.7*altura)-58)
elif sexo=="f" or sexo=="F":
    print("O valor do peso ideal para tal opção é: ", (62.1*altura)-44.7)
else:
    print("Não há peso ideal para tal opção")