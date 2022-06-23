def deDecimalParaOutra():
    lista = []
    num = int(input("Digite um número na base decimal: "))
    copiaNum = num
    print("Escolha uma base para conversão:\n1 Coverter para binário.\n2 Converter para octal.\n3 Converter para hexadecimal. ")
    opcao = int(input())
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
            lista.append(resto)
        elif quociente >= 1:
            while num > 16:
                lista.append(resto)
                num = quociente
                resto = num % 16
                quociente = num // 16
                if num <= 16:
                    lista.append(resto)
        lista = lista[-1::-1]
        numero = ""
        for i in lista:
            numero += str(i)
        return print(f"O valor {copiaNum} transformado em hexadecimal é: {numero}")


def baseAleatoriaParaDecimal():
    print("Escolha a base numérica de partida.\n1 Binário.\n2 Octal.\n3 Hexadecimal.")
    opcao = int(input())
    num = int(input("Agora, digite um número para ser convertido: "))
    copiaNum = num
    if opcao == 1:
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
        while (num // 10) >= 1:
            lista.append(num % 10)
            num = num // 10
            if num < 10:
                lista.append(num)
        lista = lista[-1::-1]
        soma = 0
        for i in range(len(lista)):
            x = (lista[(len(lista) - 1) - i]) * (16 ** i)
            soma += x
        print(f"O número Hexadecimal {copiaNum} transformado em decimal é: {soma}")



print("Escolha uma opção.\n1 Converter um número decimal para uma base qualquer.\n2 Converter de uma base qualquer para decimal.")
escolha = int(input())
if escolha == 1:
    deDecimalParaOutra()
elif escolha == 2:
    baseAleatoriaParaDecimal()