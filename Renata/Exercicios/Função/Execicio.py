'''
Escreva um programa em Python que contenha uma função que retorne True caso o
argumento passado seja primo e False caso contrário. O argumento será sempre um valor inteiro.
Peça um número, chame o método e imprima se o mesmo é número primo ou não.
'''
def verdadeiroOuFalso(n):
    validacao = True
    for i in range(2, ((n)//2)+1):
        if n % i == 0:
            validacao = False
    if validacao:
        print("É primo")
    else:
        print("Não é primo")

print("Digite um número: ")
n1 = int(input())
verdadeiroOuFalso(n1)



'''
def primo(ini, fim):
    l = []
    for k in range(ini, (fim+1)):
        cont = 0
        if -1 <= k <= 1:
            cont = 1
        for i in range(2, (k // 2) + 1):
            if k % i == 0:
                cont = 1
                break
        if cont == 0:
           l.append(k)
        else:
           pass
    return l
ini = int(input('digite o inicio: '))
fim = int(input('digite o fim'))
print(primo(ini, fim))
'''
