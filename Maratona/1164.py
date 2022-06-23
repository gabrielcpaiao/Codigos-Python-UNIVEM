'''Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos
 próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é
 igual a 6. Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 20),
 indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor
 inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito.
Para cada caso de teste de entrada, imprima a mensagem “X eh perfeito” ou “X nao eh perfeito”, de acordo com
 a especificação fornecida.
 '''
'''
N = int(input())
div = 1
soma = 0
while(N>0):
    num = int(input())
    for i in range(1,(num//2)+1):
        ePerfeito = num%div
        if(ePerfeito==0):
            soma += div
            div += 1
            print(soma)
    if (soma==num):
        print(f"{num} eh perfeito")
    else:
        print(f"{num} nao eh perfeito")
    N -= 1
'''
n = int(input())
cont = 1
while(cont<=n):
    soma = 0
    x = int(input(""))
    for i in range(1, x):
        if (x%i==0):
            soma += i
    if soma == x:
        print(f"{x} eh perfeito")
        cont += 1
    else:
        print(f"{x} nao eh perfeito")
        cont += 1