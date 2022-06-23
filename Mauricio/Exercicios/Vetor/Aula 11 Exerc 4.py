v = []*20
soma = 0
cont = 1
v.append(cont)
while True:
    v.append(soma+cont)
    x = soma + cont
    soma = cont
    cont = x
    if (x>6764):
        break
print(v)