X, Y = input(). split()
x = int(X)
y = int(Y)
cont = 1
while cont<=y:
    for i in range(x):
        print(f"{cont}", end=" ")
        cont +=1
    print(" ")