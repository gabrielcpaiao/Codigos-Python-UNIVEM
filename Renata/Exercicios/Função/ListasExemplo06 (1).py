#Funções para apagar elementos
L = ["Ana", "Roberta", "Claudio", "Antônio", "Júlia"]
print(L)
del(L[0])
print(L)
nomedel = L.pop()
print(L)
print(f"O nome apagado foi {nomedel}")
L.remove('Claudio')
print(L)
L.clear()
print(L)