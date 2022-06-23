#Gabriel Costa Paião (1 ano, 1 etapa) RA: 61876-4  Exercício 3 da Prova 1.
num_inicio_bacteria = int(input("Digite a quantidade de bactérias que havia no início: "))
dias = int(input("Digite o total de dias contabilizados: "))
cont = 1
while (cont<=dias):
    num_inicio_bacteria *= 2
    cont += 1
print(f"A população final de bactérias foi igual a: {num_inicio_bacteria}")