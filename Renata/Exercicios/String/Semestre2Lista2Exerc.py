cpf = ""

while True:
    print("Digite seu CPF (apenas números): ")
    x = input()
    if not x.isdigit():
        print("Digite apenas números!!")
    else:
        cpf += x
        break



digito1 = 0
for i in range(9):
    digito1 += int(cpf[i]) * (i+1)


restoDigito1 = digito1%11

if restoDigito1 == 10:
    digito1 = 0

digito2 = 0
for i in range(9):
    digito2 += int(cpf[i]) * (9-i)


restoDigito2 = digito2%11

if restoDigito2 == 10:
    digito2 = 0


if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
    print("CPF válido!!")
else:
    print("CPF inválido")

'''
6.	Faça um programa em Python para verificar se um CPF, digitado pelo usuário, está correto ou não. Para isto considere uma string de 11 caracteres para armazenar sem pontos ou traço, apenas números (Faça a validação para a entrada ser apenas composta de números).
A verificação do CPF está em calcular os dois dígitos de controle e comparar com os digitados, se os dois calculados forem iguais aos dois digitados, o CPF digitado é válido, caso contrário, o CPF é inválido.
Cálculo do 1º dígito: Soma os 9 primeiros números do CPF multiplicados de 1 a 9 e calcula-se o resto desta soma por 11. Se o resto for igual a 10, então o dígito é 0.
Cálculo do 2º dígito: Soma os 9 primeiros números do CPF multiplicados de 9 a 1 e calcula-se o resto desta soma por 11. Se o resto for igual a 10, então o dígito é 0.
Após o cálculo, compara-se com as respectivas posições da string e informe se o CPF é válido ou inválido.
'''

def entraCPF():
    global CPF
    while True:
        CPF = input("Informe o CPF >> ")
        if not CPF.isdigit():
            print('Digite apenas números!!')
        else:
            break

def calculaDig1():
    global dig1
    for i in range(9):
        dig1 += int(CPF[i]) * (i+1)
    dig1 %= 11
    if dig1 == 10:
        dig1 = 0
    return dig1, dig2

def calculaDig2():
    global dig2
    for i in range(9):
        dig2 += int(CPF[i]) * (9 - i)
    dig2 %= 11
    if dig2 == 10:
        dig2 = 0

def verificaCPF():
    if dig1 == int(CPF[9]) and dig2 == int(CPF[10]):
        print("CPF válido!!")
    else:
        print("CPF inválido""")


CPF = ''
dig1 = 0
dig2 = 0
entraCPF()
a = calculaDig1()
calculaDig2()
verificaCPF()
