#PESO >50 R$4 POR KILO
P = float(input("Digite o peso do peixe: "))
if (P-50>0):
    X = P - 50
    print(f"Você deverá pagar {X*4} reais de multa pois excedeu {X}Kg no peso do peixe.")