def imprimeFaixa():
    print("*-" * 15)

def verificaParImpar():
    num = int(input("Número >> "))
    imprimeFaixa()
    if num % 2 == 0:
        print("PAR")
    else:
        print("ÍMPAR")

def verificaPrimo():
    num = int(input("Número >> "))
    imprimeFaixa()
    p = True
    if -1 <= num <= 1:
        p = False
    else:
        for div in range(2, num // 2 + 1):
            if num % div == 0:
                p = False
                break
    if p:
        print('PRIMO')
    else:
        print('NÃO PRIMO')

while True:
    imprimeFaixa()
    op = int(input("1. Par ou Ímpar"
                   "\n2. Primo"
                   "\n3. Encerrar"
                   "\nOpção >> "))
    imprimeFaixa()
    if op == 3:
        break
    elif op == 1:
        verificaParImpar()
    elif op == 2:
        verificaPrimo()
    else:
        print("Opção inválida!!")