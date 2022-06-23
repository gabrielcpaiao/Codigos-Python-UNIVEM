#Meu:
num = int(input("Digite um número inteiro: "))
while(num>0):
    x = num%10
    y = (num - (x))/10
    num = y
    print(x)


#Aluno
num, rev = int(input("num: ")), 0
while num > 0:
    rev = (rev * 10) + num % 10
    num //= 10
print(f"rev: {rev}")