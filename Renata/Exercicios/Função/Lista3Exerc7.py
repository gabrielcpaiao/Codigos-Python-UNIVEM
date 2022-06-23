'''
Faça um programa que leia uma data e determine se ela é válida, ou seja, verifique se o mês está
entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e
28 dias em anos não bissextos.
Faça funções para validação e para verificar se o ano é bissexto.
'''

print("Digite uma data: ")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

validaDia = True
validaMes = True
validaTotal = True


def verificaData():
    if ano % 4 == 0 and mes == 2:
        if dia > 29:
            print("Dia inválido!")
            validaDia = False
    elif ano % 4 != 0 and mes == 2:
        if dia > 28:
            print("Dia inválido!")
            validaDia = False
    elif mes > 12:
        print("Mes inválido!")
        validaMes = False
    elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        print("Dia inválido!")
        validaDia = False
    elif dia > 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        print("Dia inválido!")
        validaDia = False
    else:
        print("Data válida")

verificaData()


'''
def validaEntrada(d):
    if len(d) != 10:
        return False
    if d[2] != '/' or d[5] != '/':
        return False
    if not d.replace('/','').isdigit():
        return False
    return True
def isbissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    return False
def validaData(d):
    dL = d.split('/')
    dia = int(dL[0])
    mes = int(dL[1])
    ano = int(dL[2])
    if 1 <= mes <= 12:
        if mes == 2: #mes com 28 ou 29 dias
            if isbissexto(ano):
                if 1 <= dia <= 29:
                    return True
            else:
                if 1 <= dia <= 28:
                    return True
        elif mes in [4, 6, 9, 11]: #meses com 30 dias
            if 1 <= dia <= 30:
                return True
        else:  #meses com 31 dias
            if 1 <= dia <= 31:
                return True
    return False
while True:
    data = input("Informe uma data no formato dd/mm/aaaa >> ")
    if validaEntrada(data):
        break
    print("Formato errado. Digite novamente...")

if validaData(data):
    print("Data válida!!")
else:
    print("Data inválida!!")
'''