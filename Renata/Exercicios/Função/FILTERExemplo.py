#FILTER
def maior_que_zero(x):
    return x > 0
valores = [10, 4, -1, 3, 5, -9, -11]
print("Números de entrada: ",valores)
print("Números positivos: ",list(filter(maior_que_zero, valores)))

#Igual ao exemplo acima usando Compreensão de Listas
print("Números positivos: ",[x for x in valores if x > 0])