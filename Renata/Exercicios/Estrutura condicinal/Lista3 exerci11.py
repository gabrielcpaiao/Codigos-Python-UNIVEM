import random
aposta = float(input("Digite a quantia a ser apostada: "))
a = random.randint(1,4)
print(a)
b = random.randint(1,4)
print(b)
c = random.randint(1,4)
print(c)
if(a!=b and a!=c and b!=c):
    print("Você perdeu!")
elif(a==b==c):
    print(f"Voce ganhou {aposta * 100} reais")
elif(a==b or b==c or a==c):
    print(f"Voce ganhou {aposta*5} reais")