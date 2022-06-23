#REDUCE
from operator import add
from functools import reduce
valores = [1, 2, 3, 4, 5]
soma = reduce(add, valores)
print("Números de entrada: ",valores)
print ("usando reduce - Soma = ",soma)
print ("usando sum - Soma = ",sum(valores))


minha_lista = [2, 4, 5, 2]
def mult(x, y):
    return x * y
produto_total = reduce(mult, minha_lista)
print("Números de entrada: ",minha_lista)
print("Valor da multiplicação dos valores: ",produto_total)