"""
x¹ + x² + x³
3   -2    5  =  20
6   -9   12  =  51
-5   0   2   =  1
b¹ = (a31/a11) * a11
b² = (a21/a11) * a11
b³ = (a32/a22) * a22
"""
m = [0] * 3
for i in range(3):
    m[i] = [0] * 4
    for j in range(4):
        if j == 3:
            m[i][j] = float(input(f"Digite o resultado da linha {i + 1} >> "))
        else:
            m[i][j] = float(input(f"Digite o valor de x{i+1}{j+1} >> "))
    print("="*37)
for i in range(3):
    for j in range(4):
        print(f"\t{m[i][j]:^5}", end = ' ')
    print()
print("="*37)
b1 = [0] * 4
b2 = [0] * 4
b3 = [0] * 4
for j in range(4):
    b1[j] = m[2][0] / m[0][0] * m[0][j]
    b2[j] = m[1][0] / m[0][0] * m[0][j]
for j in range(4):
    m[2][j] -= b1[j]
    m[1][j] -= b2[j]
for j in range(1, 4):
    b3[j] = m[2][1] / m[1][1] * m[1][j]
print(b1,b2,b3)
for j in range(1, 4):
    m[2][j] -= b3[j]
    if m[2][j] <= 10**-15:
        m[2][j] = 0
for i in range(3):
    for j in range(4):
        print(f"\t{m[i][j]:^5}", end = ' ')
    print()
print("="*37)
x3 = m[2][3] / m[2][2]
x2 = (m[1][3] - m[1][2] * x3) / m[1][1]
x1 = (m[0][3] - m[0][2] * x3 - m[0][1] * x2) / m[0][0]
print(x1, x2, x3)
