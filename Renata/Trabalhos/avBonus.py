#Gabriel Costa Paião. RA:618764. UNIVEM (Ciência da Computação 1º ano 2º semestre).

def mmc(qtdNum):
    qtdNum = int(input("Digite a quantidade de números que irão participar do cálculo do MMC: "))
    lista = []
    for i in range(qtdNum):
        x = int(input("Digite o número desejado: "))
        lista.append(x)