print('\033[31m'+'Isto é vermelho'+'\033[0;0m')
print('\033[32m'+'Isto é verde'+'\033[0;0m')
print('\033[42m'+'\033[1m'+'\033[33m'+'Isto é amarelo negrito com fundo verde'+'\033[0;0m')

'''
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'

ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'

branco = '\033[37m'

restaura cor original = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'

fundo preto = '\033[40m'
fundo vermelho = '\033[41m'
fundo verde = '\033[42m'
fundo amarelo = '\033[43m'
fundo azul = '\033[44m'
fundo magenta = '\033[45m'
fundo ciano = '\033[46m'
fundo branco = '\033[47m'
'''

from termcolor import colored

print(colored("Renata","blue"))
print(colored('*', 'green') * 100)