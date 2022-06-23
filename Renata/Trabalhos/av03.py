#Gabriel Costa Paião (Ciência da computação, UNIVEM, Noturno 1ºano, 1ºetapa) RA: 61876-4
import random
contador = 0
while (True):
    num1 = float(input("Digite um número entre 1 e 100: "))
    sorteio1 = random.randint(1, 100)
    imprimir1 = print(f"O número sorteado é {sorteio1}")
    contador += 1
    if (num1 < sorteio1):
        print("O número digitado é menor que o sorteado. Tente novamente!")
    elif (num1 > sorteio1):
        print("O número digitado é maior que o sorteado. Tente novamente!")
    else:
        print(f"Parabéns, você acertou o número sorteado. Para isso você tentou {contador} vezes.")
        break