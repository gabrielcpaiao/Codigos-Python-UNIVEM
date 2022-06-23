#Exercício 4 (Gabriel Costa Paião  RA: 61876-4)
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
med = (n1+n2)/2
if (7<=med<10):
    print("Aprovado")
elif(0<med<7):
    print("Reprovado")
elif (med==10):
    print("Aprovado com Distinção")