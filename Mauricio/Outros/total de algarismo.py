num = int(input("Digite um número inteiro: "))
retirador = 10
contador = 1
while( (num - (num%retirador) !=0) ):
    subtracao = num - (num%retirador)
    retirador *= 10
    contador+=1
print(f"O total de algarismo deste número é de: {contador}")