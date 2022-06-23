'''Horizontalizar uma matriz
Objetivo: pegar uma matriz e retornar uma lista onde cada linha segue a outra.
'''
#Código com loop tradicional
def horiz1(matriz):
   lista = []
   for row in matriz:
      for x in row:
         lista.append(x)
   return lista

#Código com compreensão de listas
def horiz2(matriz):
   return [x for row in matriz for x in row]

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(horiz1(mat))
print(horiz2(mat))
