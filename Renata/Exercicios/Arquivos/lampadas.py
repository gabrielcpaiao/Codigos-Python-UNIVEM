N = int(input())
L = input().split()
A = False
B = False
for lamp in L:
    if lamp == '1':
        A = not(A)
    else:
        A = not(A)
        B = not(B)
if A:
    print('1')
else:
    print('0')
if B:
    print('1', end="")
else:
    print('0', end="")