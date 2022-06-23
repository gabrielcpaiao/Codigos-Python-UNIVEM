'''
altura = 2*n-1
largura = n
'''
n = int(input("Digite um valor: "))
for i in range(1, n+1):
    print(f"*"*i)
for i in range(n-1, 0,-1):
    print("*"*i)