#https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/pesquisa-binaria

#fazendo a busca passando parte da lista
def pesquisa(a,elem):
  meio = len(a)//2
  if a[meio] == elem:
     return True
  if len(a) == 1:
    return False
  if elem < a[meio]:
      return pesquisa(a[:meio],elem)
  return pesquisa(a[meio:],elem)

#fazendo a busca passando os limites da lista
def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    if A[meio] == item:
        return meio
    elif item < A[meio]:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else:
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)

A = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 20))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 0))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 70))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 100))