'''Removendo vogais de uma frase
Objetivo: pegar uma ‘string’ como input e retornar uma ‘string’ sem as vogais.
'''

#Código com loop tradicional
def semVogais1(sentenca):
    vogais = 'aeiou'
    lista_filtrada = []
    for s in sentenca:
        if s not in vogais:
            lista_filtrada.append(s)
    return ''.join(lista_filtrada)

#Código com compreensão de listas
def semVogais2(sentenca):
   vogais = 'aeiou'
   return ''.join([s for s in sentenca if s not in vogais])

print(semVogais1("Semana que vem não teremos aula"))
print(semVogais2("Semana que vem não teremos aula"))
