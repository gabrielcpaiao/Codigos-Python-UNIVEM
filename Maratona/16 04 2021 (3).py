#megabyte 8.388.608 bits (chamarei de M)
#megabit 1.048.576 bits (chamarei de m)
#Exercício 3 (Gabriel Costa Paião  RA: 61876-4)
tam = float(input("Digite o tamanho do arquivo (em MB) a ser baixado: "))
tam_em_bit = tam*8388608
vel = float(input("Digite a velocidade do link de internet (em Mbps):  "))
vel_em_bit = vel*1048576
tempo = (tam_em_bit/(vel_em_bit*60))
print(f"O tempo gasto para o download deste arquivo será igual a: {tempo:.2f}min ")