#nota invalida <0 ou >10
while(True):
    nota = float(input("Digite a nota da prova: "))
    if (0<=nota<=10):
        print(f"A nota é igual a: {nota}")
        break
    else:
        print("Nota inválida")