from random import randint
#para criar pasta
import os

if not os.path.isdir("input"):
    os.mkdir("input")
if not os.path.isdir("output"):
    os.mkdir("output")

from random import randint
for i in range(1,101):
    arq_in = 'input//A_' + str(i)
    f_in = open(arq_in, 'w')
    N = randint(1,105)
    f_in.write(f"{N}\n")
    for j in range(N):
        num = randint(1,2)
        f_in.write(f"{num} ")
    f_in.close()

for i in range(1,101):
    arq_in = 'input//A_'+str(i)
    arq_out = 'output//A_'+str(i)
    f_in = open(arq_in, 'r')
    f_out = open(arq_out,'w')

    N = int(f_in.readline())
    L = f_in.readline().split()
    A = False
    B = False
    for lamp in L:
        if lamp == '1':
            A = not (A)
        else:
            A = not (A)
            B = not (B)
    if A:
        f_out.write('1\n')
    else:
        f_out.write('0\n')
    if B:
        f_out.write('1')
    else:
        f_out.write('0')
    f_in.close()
    f_out.close()
