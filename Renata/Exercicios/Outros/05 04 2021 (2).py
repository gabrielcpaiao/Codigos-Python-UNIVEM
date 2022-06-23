import random
num = random.randint(100, 999)
print(f"O número gerado foi o: {num}")
iteracao = 0
if (num//100 == (num%100)//10 == num %10):
    print("Este número não é válido")
else:
    while True:
        iteracao += 1
        a = num//100
        b = (num%100)//10
        c = num %10
        if (a > b):
            a, b = b, a
        if (b > c):
            b, c = c, b
        if (a > b):
            a, b = b, a
        print(f"O maior valor que pode ser formado com o número gerado é {c*100 + b*10 + a}")
        X = c*100 + b*10 + a
        print(f"O menor valor que pode ser formado com o número gerado é {a*100 + b*10 + c}")
        Y = a*100 + b*10 + c
        print(f"O resultado do maior número ({X}) e do menor número ({Y}) é: {X-Y}")
        if (X-Y==495):
            print(f"Foram necessárias {iteracao} iterações")
            break
        else:
            num = X-Y
#Professora
from random import randint

c = d = u = 0
while c == d == u:
    N = randint(100, 999)
    c = N // 100
    d = N % 100 // 10
    u = N % 10
print(f"Número gerado >> {N}")
cont = 0
while N != 495:
    c = N // 100
    d = N % 100 // 10
    u = N % 10
    if c > d:
        c, d = d, c
    if d > u:
        d, u = u, d
    if c > d:
        c, d = d, c

    maior = u * 100 + d * 10 + c
    menor = c * 100 + d * 10 + u
    N = maior - menor
    cont += 1
    print("=" * 40)
    print(f"Iteração: {cont}")
    print(f"Maior: {maior}\nMenor: {menor}\nN: {N}")

print(f"Foram necessárias {cont} iterações para convergir para 495")