m = [0]*5
identidade = False
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = int(input())
print()
for i in range(5):
    for j in range(5):
        print(f"{m[i][j]:^2}",end=" ")
    print()
print()
identidade = True
for i in range(5):
    if m[i][i] == 0:
        identidade = False
        break
    for j in range(5):
        if i != j and m[i][j] != 0:
            identidade = False
            break
    if not identidade:
        break

print()
if identidade:
    print("Matriz identidade!")
else:
    print("Matriz não identidade!")