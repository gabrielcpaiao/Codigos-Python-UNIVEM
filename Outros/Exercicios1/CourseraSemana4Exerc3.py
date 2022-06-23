n = int(input())
soma = 0
while True:
    soma += (n%10)
    n = n // 10
    if n == 0:
        break
print(f"{soma}")