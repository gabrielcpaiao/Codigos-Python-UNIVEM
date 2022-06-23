num = int(input())
soma = 0
for i in range(1,(num//2)+1):
    if (num%i==0):
        soma +=i
if(soma==num):
    print("Este número é perfeito")
else:
    print("Este número não é perfeito")

#Professor teste dos numero perfeitos
for num in range(1,10000):
for num in range(1 , (num//2)+1):
    if num %