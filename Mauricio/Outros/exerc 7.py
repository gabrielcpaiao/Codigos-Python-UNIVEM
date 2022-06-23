#ano bissexto ou não. Só é se for divisível por 400 ou se for divisível por 4 e não por 100
print("Digite um ano para saber se ele é bissexto:")
ano = int(input())
if ((ano%400 ==0) or ano%4==0 and ano%100!=0):
    print("O ano escolhido é bissexto")
else:
    print("O ano não é bissexto")