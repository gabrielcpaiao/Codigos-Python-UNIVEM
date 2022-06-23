lista = [1,1,2,3,2,3,3,4,5,6,5,6]
print(type(lista[0]))
for i in range(len(lista)-1):
    variavelBoleana = True
    for j in range(i+1,len(lista)):
        print(lista[i],lista[j])
        if lista[i] == lista[j] :
            variavelBoleana = False
    print()
    if variavelBoleana:
        print(lista[i])