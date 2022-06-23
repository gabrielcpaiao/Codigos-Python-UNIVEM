#LER 5 VALORES E MOSTRAR QUNTS PAR IMPAR, POSITIVO E NEGATIVO
cont = 1
par = 0
impar = 0
positivo = 0
negativo = 0
while (cont<=5):
    n = int(input(""))
    cont +=1
    if(n>0):
        positivo += 1
    if (n<0):
        negativo += 1
    if (n%2==0):
        par += 1
    if (n%2!=0):
        impar += 1
print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s")
print(f"{negativo} valor(es) negativo(s)")