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
