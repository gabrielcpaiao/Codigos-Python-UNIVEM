N = int(input())
L = [6,2,5,5,4,5,6,3,7,6]
for i in range(N):
    total = 0
    V = input()
    for dig in V:
        num = int(dig)
        total += L[num]
    print(total, 'leds')