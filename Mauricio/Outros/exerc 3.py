idade = int(input("Digite sua idade: "))
if idade<16:
    print("Proibido votar")
elif idade <18 or idade>=65:
    print("Voto é facultativo")
else:
    print("Voto obrigatório")