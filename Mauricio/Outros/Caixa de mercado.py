soma = 0
while True:
    prec = int(input("O preço deste produto é: "))
    unid = int(input(f"Digite o total de unidade comprada deste produto: "))
    if (prec==0):
        print("Este valor não existe!!")
        break
    else:
        soma += prec * unid
        print(f"O total gasto foi de: {soma}")

#professor
total = 0
while True:
    print("Digite o preço do produto (0 - encerra)")
    prec = float(input())
    if prec==0:
        break
    print("Digite a quantidade comprada: ")
    qntd = int(input())
    total += qntd * prec
if total>0:
    print("Total da compra R$: ",total)