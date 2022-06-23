'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
do mês por extenso.
Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''
num = [1,2,3,4,5,6,7,8,9,10,11,12]
mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
data = input("Digite sua data de nascimento (dd/mm/aaaa): ").split("/")
data[1] = int(data[1])
print(data[1])
print(type(data[1]))
print(f"Você nasceu em {data[0]} de {mes[data[1]-1]} de {data[2]}.")