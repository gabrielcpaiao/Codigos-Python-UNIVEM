num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
cont1 = 0
for i in range(1, (num1//2)+1):
    if num1%i==0:
        print(i)
        cont1 += i
print(f"O valor final é igual a {cont1}")

cont2 = 0
for i in range(1, (num2//2)+1):
    if num2%i==0:
        print(i)
        cont2 += i
print(f"O valor final é igual a {cont2}")

if cont1 == num2 or cont2 == num1:
    print("Estes números são números amigos")
else:
    print("Estes númro não são número amigos")