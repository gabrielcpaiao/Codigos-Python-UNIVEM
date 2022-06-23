#Gabriel Costa Paião (RA: 61876-4). Ciência da Computação, 1º ano, 1º etapa, noturno.
#Genésio Henrique (Ra: 615536)
#Enrico Pinarelli (RA- 615579)
from random import randint
import time
L = []
T = []
I = 5000
while I <= 50000:
    for i in range (1, I):
        L.append(randint(1, I))
    ini = time.time()
    L.sort()
    fim = time.time()
    tempo = fim - ini
    T.append(tempo)
    I += 5000
I = 5000
for i in range (10):
    print(f"Tamanho: {I} >> Tempo: {T[i]}")
    I += 5000