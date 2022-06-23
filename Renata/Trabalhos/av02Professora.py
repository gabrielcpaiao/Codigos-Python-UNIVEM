'''
Faça um programa que peça o cadastro de uma senha.
Faça a validação, imprimindo “Senha válida” ou “Senha inválida”.
Para validar a senha, ela tem que ter exatamente 8 caracteres,
sendo pelo menos 1 letra maiúscula, 1 número e 1 caractere especial.

Exemplos de senhas válidas
Ren@ta21
Progr@3@
test3SE!
prof@Un1
'''
from random import randint, choice, sample
from termcolor import colored


def geraSenha():
    ce = ['@','&','!','#','%','*','?']
    senha = ''
    senha += chr(randint(65,90))
    senha += str(randint(0,9))
    senha += choice(ce)
    for i in range(2):
        senha += str(randint(0,9))
    for i in range(3):
        senha += chr(randint(97,122))
    senha = ''.join(sample(senha, len(senha)))
    return senha

tent = 1
while True:
    valida = True
    contM = contN = contCE = 0
    print("~" * 44)
    senha = input('Insira uma senha de 8 caracteres >> ')
    print("~" * 44)
    tent += 1
    if len(senha) != 8:
        valida = False
    for c in senha:
        if c.isupper():
            contM += 1
        if c.isdigit():
            contN += 1
        if not c.isalnum():
            contCE += 1
    if contM == 0 or contN == 0 or contCE == 0:
        valida = False
    if tent <= 3:
        if valida:
            print(colored("Senha cadastrada com sucesso!!","blue"))
            break
        else:
            print(colored("Senha inválida!!","red"))
    else:
        print(colored("Você esgotou o número de tentativas", "red"))
        senha = geraSenha()
        print(f"Senha gerada aleatoriamente >> {senha}")
        resp = input("Deseja usar essa senha? [S/N] >> ").upper()[0]
        if resp == 'S':
            print("~" * 44)
            print(colored("Senha cadastrada com sucesso!!","blue"))
        break