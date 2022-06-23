from random import randint
cont = 1
maior = 0
menor = 51
while(cont<=20):
    x = randint(1, 50)
    print(f"O número sorteado é: {x}")
    cont += 1
    if (x>maior):
        maior = x
    if (x<menor):
        menor = x
print(f"O maior número sorteado foi o {maior} e o menor número sortedo foi o {menor}")