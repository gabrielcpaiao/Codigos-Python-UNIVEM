'''
Qual é o número qe possui como divisores todos os numeros de 1 a 15
'''
n = 1
div = 1
while (div <= 20):
    if (n % div == 0):
        div += 1
    else:
        n += 1
        div = 1
print(n)