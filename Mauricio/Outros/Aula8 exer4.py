#ver se é primo com for
num = int(input())
validacao = True
for i in range(1,num+1):
    x = num%i
    if (x==0):
        print (i)
        validacao = False
if validacao:
    print("O número é primo")
else:
    print("O número não é primo")

#professor
num = int(input())
cont = 0
for i in range(1,num+1):
    if num%i == 0:
        cont+=1
if cont==2:
    print("O número em questão é primo")
else:
    print("O número em questão não é primo")