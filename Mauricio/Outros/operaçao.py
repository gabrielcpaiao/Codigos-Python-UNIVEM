while True:
    oper = (input("Digite a operação desejada (+, -, *, / e #): "))
    if oper == '#':
        break
    n1 = float(input("Digite o primeiro operando: "))
    n2 = float(input("Digite o segundo operando: "))
    if oper=='+':
        print(f"{n1} + {n2} = {n1+n2}")
    elif oper =='-':
        print(f"{n1} - {n2} = {n1 - n2}")
    elif oper == '*':
        print(f"{n1} * {n2} = {n1 * n2}")
    elif oper == '/':
        if n2 ==0:
            print("Esta divisão é uma indeterminação matemática!")
        else:
            print(f"{n1} / {n2} = {n1 / n2}")