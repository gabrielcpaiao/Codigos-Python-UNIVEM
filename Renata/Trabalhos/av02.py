#Gabriel Costa Paião   RA: 61876-4. Ciência da computação     UNIVEM   noturno    (1º ano, 1º semestre 2021)
print("Digite o primeiro número inteiro e positivo entre 0 e 999")
A = int(input())
print("Digite o segundo número inteiro e positivo entre 0 e 999")
B = int(input())
if ((A<0 or A>999) and (B<0 or B>999)):
    print("O número digitado está errado")
elif (((A%10) + (B%10) > 9) and ((A//10)%10 + (B//10)%10 >=9) and ((A//100) + (B//100)>=9)):
    U = 1
    D = 1
    C = 1
    print("3 vai 1")
elif (((A%10) + (B%10) > 9) and ((A//10)%10 + (B//10)%10 >=9)):
    U = 1
    D = 1
    print("2 vai 1")
elif (((A%10) + (B%10) > 9)):
    U = 1
    print("1 vai 1")
elif ((A//10)%10 + (B//10)%10 >9) and ((A//100) + (B//100)>=9):
    D = 1
    C = 1
    print("2 vai 1")
elif (A//10)%10 + (B//10)%10 >9:
    D = 1
    print("1 vai 1")
elif ((A//100) + (B//100)>9):
    C = 1
    print("1 vai 1")
else:
    print("0 vai 1")