from random import randint

a = [0] * 5
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(randint(1, 10))
print(a)
print("Triangulo Superior esquerdo")
for i in range(5):
    for j in range(5):
        if i+j<=3:
            print(a[i][j])
#Solução ótima:
for i in range(4):
    for j in range(4-i):
        print(a[i][j])
'''
from random import randint

a = [0] * 5
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(randint(1, 10))
print(a)
print("Triangulo Superior esquerdo")
for i in range(5):
    for j in range(5):
        if(i+j<=3):
            print(a[i][j])
'''