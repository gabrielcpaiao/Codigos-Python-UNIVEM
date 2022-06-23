print("Informe a quantidade dos ingredientes que você tem para o bolo")
A = int(input("Xícaras de farinha de trigo >> "))
B = int(input("Ovos >> "))
C = int(input("Colheres de leite >> "))
A = A // 2
B = B // 3
C = C // 5
if A < B and A < C:
    print(f"Produzirá {A} bolos")
elif B < C:
    print(f"Produzirá {B} bolos")
else:
    print(f"Produzirá {C} bolos")