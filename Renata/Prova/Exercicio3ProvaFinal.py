a = 0
b = 1
j = 0
while a != b:
    for i in range(6):
        while j <= i:
            print(j,end="")
            j += 1
    b = a
    print(i,end="")