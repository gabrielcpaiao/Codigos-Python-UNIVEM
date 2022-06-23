#Gabriel Costa Paião   RA:61876-4
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if (n1%n2==0):
    while True:
        cont = 1
        x = n1 * cont
        y = n2 * cont
        if (x==y):
            print(f"O MMC de {n1} e de {n2} é igual a {x}")
            break
        else:
            cont += 1
else:
    print("O primeiro valor não pode ser dividido pelo segundo.")