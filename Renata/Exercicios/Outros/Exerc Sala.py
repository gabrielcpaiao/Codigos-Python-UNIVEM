#num entre 100 e 999 somar algarismo par e mult algarismos impar. imprimir a lista de 100 a 999
for i in range (100,1000):
    u = i %10
    d = (i %100)//10
    c= i //100
    if (u%2==0):
        print(f"{i} = {u + d +c}")
    else:
        print(f"{i} = {u * d *c}")

#Aluno:
for i in range (100,1000):
    cent = i//100
    dez = (i%100)//10
    unidade = i%10
    if i % 2 == 0:
        print(f"{i} = {cent+dez+unidade}")
    else:
        print(f"{i} = {cent*dez*unidade}")