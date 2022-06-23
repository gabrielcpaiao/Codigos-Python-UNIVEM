#c = cabine
#a = total de alunos
#calc o minimo de viagens
c = int(input())
a = int(input())
x = a // (c-1)
if (a % (c-1)>0):
    print(f"{x+1}")
else:
    print(f"{x}")