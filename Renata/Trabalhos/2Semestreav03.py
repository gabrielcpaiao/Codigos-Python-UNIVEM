#Gabriel Costa Paião. RA:618764. UNIVEM (Ciência da Computação 2021 1º ano 2º semestre).
#validar a hora de escolher as opções
#validar a entrada das bases (na 1º função já está feito)

'''
Fazer um programa em Python que tenha uma função para transformar números de uma
base decimal para qualquer outra base e uma função de qualquer outra base para base
decimal. Considerar as bases binário, octal, decimal e hexadecimal.
O programa deverá fazer a entrada de dados, no qual o usuário poderá escolher qual
conversão ele irá fazer ou optar por sair. Repetir até ele desejar parar as conversões.
Peça o número, a base de origem e a base destino. Faça a chamada aos métodos
necessários e imprima o valor convertido para a base desejada. Faça a validação para o
número digitado ter apenas dígitos válidos para a base.
Obs.: O seu programa pode ter quantas funções forem necessárias, mas para a
transformação das bases façam apenas 2 funções.
'''

def deDecimalParaOutra():
    lista = []
    print("Escolha uma base para conversão:\n1 Coverter para binário.\n2 Converter para octal.\n3 Converter para hexadecimal. ")
    opcao = int(input())
    while True:
        num = input("Digite um número na base decimal: ")
        if not num.isdigit():
            print("Número inválido. Digite apenas números.")
        else:
            break
    num = int(num)
    copiaNum = num
    if opcao == 1:
        quociente = num // 2
        resto = num % 2
        if quociente == 0:
            lista.append(resto)
        elif quociente >= 1:
            while num != 1:
                lista.append(resto)
                num = quociente
                resto = num % 2
                quociente = num // 2
                if num == 1:
                    lista.append(resto)
        lista = lista[-1::-1]
        numero = ""
        for i in lista:
            numero += str(i)
        return print(f"O valor {copiaNum} transformado em binário é: {numero}")
    elif opcao == 2:
        quociente = num // 8
        resto = num % 8
        if quociente == 0:
            lista.append(resto)
        elif quociente >= 1:
            while num > 8:
                lista.append(resto)
                num = quociente
                resto = num % 8
                quociente = num // 8
                if num <= 8:
                    lista.append(resto)
        lista = lista[-1::-1]
        numero = ""
        for i in lista:
            numero += str(i)
        return print(f"O valor {copiaNum} transformado em octal é: {numero}")
    elif opcao == 3:
        quociente = num // 16
        resto = num % 16
        if quociente == 0:
            if resto == 15:
                lista.append("F")
            elif resto == 14:
                lista.append("E")
            elif resto == 13:
                lista.append("D")
            elif resto == 12:
                lista.append("C")
            elif resto == 11:
                lista.append("B")
            elif resto == 10:
                lista.append("A")
        elif quociente >= 1:
            while num > 16:
                if resto == 15:
                    lista.append("F")
                elif resto == 14:
                    lista.append("E")
                elif resto == 13:
                    lista.append("D")
                elif resto == 12:
                    lista.append("C")
                elif resto == 11:
                    lista.append("B")
                elif resto == 10:
                    lista.append("A")
                else:
                    lista.append(resto)
                num = quociente
                resto = num % 16
                quociente = num // 16
                if num <= 16:
                    if resto == 15:
                        lista.append("F")
                    elif resto == 14:
                        lista.append("E")
                    elif resto == 13:
                        lista.append("D")
                    elif resto == 12:
                        lista.append("C")
                    elif resto == 11:
                        lista.append("B")
                    elif resto == 10:
                        lista.append("A")
                    else:
                        lista.append(resto)
        lista = lista[-1::-1]
        numero = ""
        for i in lista:
            numero += str(i)
        return print(f"O valor {copiaNum} transformado em hexadecimal é: {numero}")


def baseAleatoriaParaDecimal():
    print("Escolha a base numérica de partida.\n1 Binário.\n2 Octal.\n3 Hexadecimal.")
    opcao = int(input())
    if opcao == 1:
        validacao = True
        while validacao:
            num = input("Digite um número na base binária: ")
            for i in num:
                if i == "1" or i == "0":
                    validacao = False
                else:
                    print("Número inválido. Digite apenas 0 ou 1.")
                    validacao = True
                    break
        num = int(num)
        copiaNum = num
        lista = []
        while (num // 10) >= 1:
            lista.append(num % 10)
            num = num // 10
            if (num//10) < 1:
                lista.append(num % 10)
        lista = lista[-1::-1]
        soma = 0
        for i in range(len(lista)):
            x = (lista[(len(lista)-1)-i]) * (2**i)
            soma += x
        print(f"O número binário {copiaNum} transformado em decimal é: {soma}")
    elif opcao == 2:
        lista = []
        validacao = True
        while validacao:
            num = input("Digite um número na base octal: ")
            for i in num:
                if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
                    validacao = False
                else:
                    print("Número inválido. Digite apenas 0 ou 1.")
                    validacao = True
                    break
        num = int(num)
        copiaNum = num
        while (num // 10) >= 1:
            lista.append(num % 10)
            num = num // 10
            if num < 10:
                lista.append(num)
        lista = lista[-1::-1]
        soma = 0
        for i in range(len(lista)):
            x = (lista[(len(lista) - 1) - i]) * (8 ** i)
            soma += x
        print(f"O número octal {copiaNum} transformado em decimal é: {soma}")
    elif opcao == 3:
        lista = []
        validacao = True
        while validacao:
            num = input("Digite um número na base hexadecimal: ")
            for i in num:
                if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == "F":
                    validacao = False
                else:
                    print("Número inválido.")
                    validacao = True
                    break
        copiaNum = num

        print(num)
        num1 = num[-1::-1]
        print(num1)
        expoente = 0
        soma = 0

        for i in num1:
            if i =="A":
                soma += 10 * (16 ** expoente)
                expoente += 1
            elif i =="B":
                soma += 11 * (16 ** expoente)
                expoente += 1
            elif i =="C":
                soma += 12 * (16 ** expoente)
                expoente += 1
            elif i =="D":
                soma += 13 * (16 ** expoente)
                expoente += 1
            elif i =="E":
                soma += 14 * (16 ** expoente)
                expoente += 1
            elif i =="F":
                soma += 15 * (16 ** expoente)
                expoente += 1
            else:
                soma += int(i)*(16**expoente)
                expoente += 1

        print(f"O número Hexadecimal {copiaNum} transformado em decimal é: {soma}")




print("Escolha uma opção.\n1 Converter um número decimal para uma base qualquer.\n2 Converter de uma base qualquer para decimal.")
escolha = int(input())
if escolha == 1:
    deDecimalParaOutra()
elif escolha == 2:
    baseAleatoriaParaDecimal()