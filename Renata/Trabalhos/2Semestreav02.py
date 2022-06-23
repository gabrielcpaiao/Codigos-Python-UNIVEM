#Gabriel Costa Paião (RA: 618764) 1º ANO 2º Semestre. Ciência da Computação UNIVEM.

'''
Faça um programa que peça o cadastro de uma senha.
Para isso crie as funções para:

Testar a senha, retornando True ou False caso seja válida ou inválida, respectivamente.
Para a senha ser válida, ela tem que ter exatamente 8 caracteres,sendo pelo menos 1 letra
maiúscula, 1 número e 1 caractere especial.

 Sugerir uma senha válida aleatória. Chame essa função caso a senha digitada pelo usuário
seja inválida.

Exemplos de senhas válidas
Ren@ta21
Progr@3@
test3SE!
prof@Un1
Permita que o usuário tente, no máximo, 3 vezes o cadastro da senha. Se entrar com uma senha
válida emita uma mensagem de senha cadastrada e encerre o programa. Se não entrar com
nenhuma válida chame a função que gere uma senha válida e mostre ao usuário perguntando se
deseja utilizar a senha ofertada. Emita a mensagem de senha cadastrada, caso aceite ou mensagem
de senha não cadastrada caso não aceite e encerre o programa.
'''
from random import randint
deuCerto = True

def testeSenha():
    global deuCerto
    deuCerto = True
    caractereEspecial = ["!", "@", "#", "$", "%", "&", "*", "(", ")"]
    tentativas = 1
    while tentativas <=3:
        print("Digite uma senha de oito caractere contendo um caractere especial, uma letra maiúscula e um número: ")
        while True:
            senha = input()
            if len(senha) != 8:
                print("\nA senha deve conter oito caracteres!")
            else:
                break
        contadorDeCaractereEspecial = 0
        contadorDeNumero = 0
        contadorDeMaiuscula = 0
        for i in senha:
            if i in caractereEspecial:
                contadorDeCaractereEspecial += 1
            elif i.isupper():
                contadorDeMaiuscula += 1
            elif i.isdigit():
                contadorDeNumero += 1
        if contadorDeCaractereEspecial >= 1 and contadorDeNumero >=1 and contadorDeMaiuscula >=1:
            print("\nSenha cadastrada!")
            break
        else:
            print("\nSenha inválida. A senha deve conter 8 caracteres, sendo um caractere especial, uma letra maiúscula e um número.\n")
            tentativas += 1
            deuCerto = False


novaSenha = ""
aceitarNovaSenha = ""
def sugereSenha():
    global aceitarNovaSenha
    global novaSenha
    for i in range(5):
        novaSenha += chr(randint(97,122))
    novaSenha += str(chr(randint(48,57)))
    novaSenha += chr(randint(33,47))
    novaSenha += chr(randint(65,90))
    print(f"Senha suredida: {novaSenha}")
    aceitarNovaSenha = input("Digite 'sim' para aceitar a senha criada ou 'não' para recusar: ").lower()
    if aceitarNovaSenha == "sim":
        print("Senha cadastrada!")
    else:
        print("Senha não cadastrada!")

testeSenha()
if not deuCerto:
    sugereSenha()



'''
from random import randint, choice, sample
from termcolor import colored

def geraSenha():
    ce = ['@','&','!','#','%','*','?']
    senha = chr(randint(65,90))
    senha += str(randint(0,9))
    senha += choice(ce)
    for i in range(2):
        senha += str(randint(0,9))
    for i in range(3):
        senha += chr(randint(97,122))
    senha = ''.join(sample(senha, len(senha)))
    return senha

def validaTamanho(n):
    if len(n) != 8:
        return False
    return True
def validaNum(n):
    for c in n:
        if c.isnumeric():
           return True
    return False
def validaLetraM(n):
    for c in n:
        if c.isupper():
            return True
    return False
    #Outra forma
    
    if not any(c.isupper() for c in n):
        return False
    return True
    
def validaCE(n):
    for c in n:
        if not c.isalnum():
            return True
    return False

tent = 1
while True:
    if tent <= 3:
        print("~" * 44)
        senha = input('Insira uma senha de 8 caracteres >> ')
        print("~" * 44)
        if validaTamanho(senha) and validaNum(senha) and validaLetraM(senha) and validaCE(senha):
            print(colored("Senha cadastrada com sucesso!!","blue"))
            break
        else:
            print(colored("Senha inválida!!","red"))
    else:
        print(colored("Você esgotou o número de tentativas","red"))
        senha = geraSenha()
        print(f"Senha gerada aleatoriamente >> {senha}")
        resp = input("Deseja usar essa senha? [S/N] >> ").upper()[0]
        print("~" * 44)
        if resp == 'S':
            print(colored("Senha cadastrada com sucesso!!","blue"))
        else:
            print(colored("Senha não cadastrada!!", "red"))
        break
    tent += 1
'''