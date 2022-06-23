from random import randint

num = int(input('Digite o número da base decimal que desaja alterar >> '))

print(
    'Escolha qual base deja converter >> \n1 Converter para Binário \n2 Convereter para Octal \n3 Converter para Hexadecimal n\4 Converter para decimal ')

op = int(input('Opção escolhida >> '))
if op == 1:
    print(f'{num} convertido para binário é {bin(num)[2:]}')
elif op == 2:
    print(f'{num} comvertido para octal {oct(num)[2:]}')
elif op == 3:
    print(f'{num} convertido para hexadecimal {hex(num)[2:]}')
else:
    print('Opção inválida')

num = str(input('Digite o número da base binario que desa altrar >> '))

print(f'{num} convertido para decimal é {int(num, 2)}')

num = str(input('Digite o número da base octal que desa altrar >> '))

print(f'{num} convertido para decimal é {int(num, 8)}')

num = str(input('Digite o número da base hexa que desa altrar >> '))

print(f'{num} convertido para decimal é {int(num, 16)}')