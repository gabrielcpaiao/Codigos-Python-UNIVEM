num = int(input())
valBoleana = True
for i in range(2, num):
    if num % i == 0:
        print(f"O número {num} não é primo.")
        valBoleana = False
        break


if valBoleana:
    print(f"O número {num} é primo.")