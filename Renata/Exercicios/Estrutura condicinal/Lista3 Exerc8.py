print("Digite uma data válida: ")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))
if(1<=mes<=12):
    if(mes== 1 or mes== 2 or mes== 3 or mes== 5 or mes== 7 or mes== 8 or mes== 10 or mes== 12):
        if(mes== 2 and ano%4== 0 and ano % 100 != 0 and ano % 400 == 0):
            if(1<=dia<=29):
                print("Data válida!")
            else:
                print("Data inválida!")
        elif(mes==2 and 1<=dia<=28):
            print("Data válida!")
        else:
            print("Data inválida!")
    elif(1<=dia<=30):
        print("Data válida!")
    else:
        print("Data inválida!")
else:
    print("Mês inválido!")