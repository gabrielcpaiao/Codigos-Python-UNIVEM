print("Digite o valor da compra")
vc = float(input())
if (vc >= 500):
    desc = vc * 0.2
elif (vc >=200):
    desc = vc * 0.15
else:
    desc = vc *0.1

vp = vc - desc
print("Valor da compra R$", vc)
print("Desconto  de R$", desc)
print("Total a pagar R$",vp)