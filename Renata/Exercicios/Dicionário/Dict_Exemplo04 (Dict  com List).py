'''
Faça um cadastro de aluno para armazenar nome, nota 1 e nota 2,
onde o nome seja o índice
Armazene as duas notas em uma lista e a lista no dicionário
Imprima todo o dicionário
'''
notas = {}
while True:
    listaN = []
    nomeAluno = input("Informe o nome do aluno, fim para encerrar: ")
    if nomeAluno == "fim":
        break
    if nomeAluno in notas:
        print("Aluno já cadastrado")
    else:
        nota1 = float(input("Informe a nota 1: "))
        nota2 = float(input("Informe a nota 2: "))
        listaN.append(nota1)
        listaN.append(nota2)
        notas[nomeAluno] = listaN
print(notas)


for aluno in notas: #somente as chaves
    print(aluno)

for aluno in notas.keys(): #somente as chaves
    print(aluno)

for nota in notas.values(): #somente os valores
    print(nota)

print("Notas dos alunos")
for aluno, nota in notas.items(): #chaves e valores
    print("="*15)
    print("Nome: ",aluno)
    print("Nota 1: {:.2f}".format(nota[0]))
    print("Nota 2: {:.2f}".format(nota[1]))
    print("Média : {:.2f}".format(sum(nota)/len(nota)))
