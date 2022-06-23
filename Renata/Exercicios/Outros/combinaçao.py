#calcular o numero de listas
import math
num = int(input("Digite o total de elementos que deseja para criar suas listas: "))
lista = int(input("Digite o tamanho da lista que deseja: "))
condicao = input("Digite (S) se a lista tiver elementos repetidos ou digite (N) se a lista não tiver elementos repetidos: ")
if (condicao == "S"):
    print("O número de listas que podem ser criadas é", num**lista)
else:
    print("O número de listas que podem ser criadas é", )