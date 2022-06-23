from random import randint
m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = randint(1,1)
        print(f"{m[i][j]:^2}",end=" ")
    print()
print()
simetrica = True
for i in range(5):
    for j in range(5):
        if i != j:
            if m[i][j] != m[j][i]:
                simetrica = False
                break
    if not simetrica:
        break

if simetrica:
    print("A matriz é simétrica!")
else:
    print("A matriz não é simétrica!")