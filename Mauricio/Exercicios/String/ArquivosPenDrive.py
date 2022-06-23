'''
Tem uma lista de arquivo p colocar no pendrive.
Quero armazenar a maior quantidade possível.
Sei o tamanho de cada arquivo e do pendrive.
Mostrar quantos e quais asquivos que serão inseridos e o espaço que sobrou.
Pegar os menores.
'''

arq = []
while True:
    nome = input("Digite o nome do arquivo ou FIM: ")
    if nome != "FIM":
        tam = int(input("Digite o tamanho do arquivo: "))
        x = [tam,nome]
        arq.append(x)
    else:
        break
arq.sort()

pen = []
cap = int(input("Digite a capacidade do PenDrive: "))
quais = []
for i in range(len(arq)):
    if cap > arq[i][0]:
        pen.append(arq[i][0])
        quais.append(arq[i][1])
        cap -= arq[i][0]

print(f"Foram inseridos {len(pen)} arquivos.")
print(f"O valores dos arquivos inseridos é: {pen}")
print(f"Os arquivos inseridos foram os: {quais}")
print(f"O total de memória que restou no Pendrive foi de {cap} Kbytes.")