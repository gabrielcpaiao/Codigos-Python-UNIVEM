#Gabriel Costa Paião (RA: 61876-4). Ciência da computação, 1º ano e 1º etapa.
from random import randint
surpresa = []
while len(surpresa) != 6:
    n = int(randint(1,60))
    if n not in surpresa:
        surpresa.append(n)
surpresa.sort()
print("A SURPRESINHA gerada é: ")
print(surpresa)
megasenha = []
print("Digete 6 valores diferentes: ")
while len(megasenha) != 6:
    x = int(input(""))
    if x not in megasenha:
        megasenha.append(x)
megasenha.sort()
print("Os valores da MEGASENA são: ")
print(megasenha)
resultado = []
for i in range(6):
    for j in range(6):
        if megasenha[i]==surpresa[j]:
            resultado.append(surpresa[j])
if len(resultado)==4:
    print("O jogador acertou a Quadra (obteve 4 acertos).")
elif len(resultado)==5:
    print("O jogador acertou a Quina (obteve 5 acertos).")
elif len(resultado)==6:
    print("O jogador acertou a Sena (obteve 6 acertos).")
else:
    print(f"O jogador obteve {len(resultado)} acertos.")