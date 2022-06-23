for z in range(100,1000):
    x = 0
    for y in range(2,z):
        if z % y == 0:
            x += 1
    if x == 0:
        print(z)