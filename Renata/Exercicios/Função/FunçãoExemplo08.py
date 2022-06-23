def validaNum(n):
    if n > 999:
        return False
    return True

num = int(input("Número >> "))
if validaNum(num):
    c = num // 100
    d = num % 100 // 10
    u = num % 10
    print(c, d, u)
else:
    print("Número inválido!!")