from termcolor import colored

def validaEntrada(num,base):
    for i in range(len(num)):
        if num[i] not in aldigit[:base]:
           return False
    return True

def decToqq(num,base):
    l = []
    num = int(num)
    while num != 0:
        l.append(aldigit[num % base])
        num //= base
    l = l[::-1]
    num = "".join(l)
    return num

def qqTodec(num,base):
    dec = 0
    j = len(num)-1
    for i in range(len(num)):
        dec += aldigit.index(num[i]) * base ** j
        j -= 1
    return dec

aldigit = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#ou
#aldigit = '0123456789ABCDEF'
while True:
    print("~" * 50)
    baseO = int(input("Informe a base inicial: "))
    while True:
        numero = input("Informe o número que deseja converter: ").upper()
        if baseO == 16:
            if numero.isalnum() and validaEntrada(numero, baseO):
                break
            else:
                print(f"Números inválidos para a base {baseO}")
        elif numero.isdigit():
            if validaEntrada(numero, baseO):
                break
            else:
                print(f"Números inválidos para a base {baseO}")
        else:
            print("Informe apenas números")

    baseD = int(input("Informe a base final: "))
    if baseO != 10 and baseD != 10:
        dec = qqTodec(numero,baseO)
        conv = decToqq(dec,baseD)
    elif baseO == 10:
        conv = decToqq(numero,baseD)
    else:
        conv = qqTodec(numero, baseO)

    print(colored(f"O número {numero} na base {baseO} é {conv} na base {baseD}","blue"))
    print("~" * 50)
    resp = input("Deseja converter mais um número? [S/N] -> ").upper()[0]
    if resp != 'S':
        break