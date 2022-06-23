indPol = float(input("Digite o índice de poluição: "))
if (0.3<=indPol<0.4):
    print("As empresas do primeiro grupo devem suspender suas atividades!")
elif (0.4<=indPol<0.5):
    print("As empresas do primeiro e do segundo grupo devem suspender suas atividades!")
else:
    print("Todos os grupos devem suspender suas atividades!")