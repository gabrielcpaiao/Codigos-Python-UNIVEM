#Parâmetros e retorno

def calcMed(a, b):
    media = (a + b) / 2
    return media


nota1 = float(input("Nota 1 >> "))
nota2 = float(input("Nota 2 >> "))
m = calcMed(nota1, nota2)
if m >= 6:
    print(f"Aprovado com a média {m}")
else:
    print(f"Reprovado com a média {m}")