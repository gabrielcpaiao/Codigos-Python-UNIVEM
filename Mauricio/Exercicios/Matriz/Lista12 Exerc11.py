from random import randint
m = [0]*4
tp = []
maiorsemana = 0
mm = 0
ms = 0
for i in range(4):
    m[i] = [0]*12
    for j in range(12):
        m[i][j] = randint(1,70)
        if m[i][j] > maiorsemana:
            mm = j
            ms = i
print(f"O mês {mm} e a semana {ms} foi aonde ocorreu o maior pico de produção.")
for i in range(4):
    for j in range(12):
        print(f"{m[i][j]:^5}", end=" ")
    print()
#Letra a
maior = 0
for i in range(12):
    soma = 0
    for j in range(4):
        soma += m[j][i]
    tp.append(soma)
print()
print()
maior = 0
mes = 0
for i in range(12):
    print(f"O total de peças produzidas no mês {i+1} foi igual a: {tp[i]} peças.")
    if tp[i]>maior:
        maior = tp[i]
        mes = i
#Letra b
print()
soma = 0
for n in range(12):
    soma += tp[n]
print(f"O total de peças produzidas no ano é igual a: {soma} peças.")
#Maior produção
print()