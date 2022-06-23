from math import factorial
operacao = int(input("Digite 1 para fazer uma operação de Combinação e 2 para fazer uma operação de Permutação: "))
if (operacao==1):
    n = int(input(""))
    r = int(input(""))
    C = factorial(n)/(factorial(r)*factorial(n-r))
    print(f"O resultado desta combinação é: {C}")
elif (operacao==2):
    n = int(input(""))
    r = int(input(""))
    if (n>r):
        P = factorial(n)/factorial(n-r)
        print(P)
    elif(n==r):
        P = factorial(n)
        print(P)

Italo
from math import factorial
while True:
    n, r = map(int, input("N e R: ").split())
    fn, fr, fnr = factorial(n), factorial(r), factorial(n - r)
    if input("(P)ermutação ou (C)ombinação? ")[0].lower() == 'c':
        print(f"Resultado (Combinação): {fn // (fnr * fr)}")
    elif n > r:
        print(f"Resultado (Permutação N > R): {fn // fnr}")
    elif n == r:
        print(f"Resultado (Permutação N == R): {fn}")
    else:
        print("Input invalido (Permutação N < R)")
    if input("Repetir? ")[0].lower() != 's':
        break