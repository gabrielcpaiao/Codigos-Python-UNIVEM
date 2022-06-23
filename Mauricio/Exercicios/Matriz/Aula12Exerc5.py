from random import randint

a = [0] * 5
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(randint(1, 100))
print(a)
print("Triangulo Inferior direito")
for i in range(5):
    for j in range(5):
        if i+j>=5:
            print(a[i][j])
#Solução ótima:
for i in range(1, 5):
    for j in range(5-i, 5):
        print(a[i][j])