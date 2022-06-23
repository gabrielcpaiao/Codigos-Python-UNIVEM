from random import randint
m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = randint(1,10)
        print(f"{m[i][j]:^2}",end=" ")
    print()
print()
print("Elementos da diagonal secundária: ")
for i in range(5):
    for j in range(5):
        if i+j == 4:
            print(f"{m[i][j]:^2}",end=" ")