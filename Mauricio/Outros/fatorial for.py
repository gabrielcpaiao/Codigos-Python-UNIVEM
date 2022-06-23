print("Digite um númro: ")
num = int(input())
if (num<0):
    print("Não existe fatorial!!")
else:
    fat = 1
    for i in range (num , 0 , -1):
        fat*= i
    print("Fatorial =", fat)