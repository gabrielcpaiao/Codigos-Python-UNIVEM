#Gabriel Costa Paião (1 ano, 1 etapa) RA: 61876-4  Exercício 1 da Prova 1.
HI = int(input("Digite o horário que começou o jogo de xadrez: "))
HF = int(input("Digite o horário que terminou o jogo de xadrez: "))
if (HF<=HI):
    DIA1 = 24-HI
    print(f"O tempo de duração total deste jogo foi de: {DIA1+HF} horas")
else:
    print(f"O tempo de duração total deste jogo foi de: {HF-HI} horas")