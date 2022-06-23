#Gabriel Costa Paião (RA:618764). Ciência da Computação. UNIVEM. 1º ano e 1º etapa, Noturno.
#Prova Final --> Exercício (2)
m = [0]*10
for i in range(10):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = 2**(i)
        print(f"{m[i][j]:^3}",end=" ")
    print()