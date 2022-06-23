sal = float(input("Digite o salário de um trabalhador: "))
prestacao = float(input("O valor da prestação do empréstimo é: "))
if(prestacao>sal*0.2):
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")