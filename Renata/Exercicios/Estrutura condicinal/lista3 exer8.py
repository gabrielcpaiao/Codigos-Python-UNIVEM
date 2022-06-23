print("Informe uma data")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
valid = False
if 1 <= mes <= 12:
    if mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if 1 <= dia <= 29:
                valid = True
        else:
            if 1 <= dia <= 28:
               valid = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 1 <= dia <= 30:
            valid = True
    else:
        if 1 <= dia <= 31:
            valid = True
if valid:
    print("Data válida!!")
else:
    print("Data inválida!!")