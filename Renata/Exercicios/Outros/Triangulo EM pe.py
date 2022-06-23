'''
Altura e lado n
base 2*n-1
'''
n = int(input("Digite um valor: "))
for i in range(1, n+1, 2):
    print(("*"*i).center(2*n-1))