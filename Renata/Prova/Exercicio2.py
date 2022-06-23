num = int(input())
soma = 0
impar = 1
while soma < num:
    soma += impar
    impar += 2
if soma == num:
    print("Quadrado perfeito")