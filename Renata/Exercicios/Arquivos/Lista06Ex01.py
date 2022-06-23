'''
Considere o arquivo notas_estudantes.txt que contém uma
linha para cada aluno de uma turma de estudantes.
O nome de cada estudante está no início de cada linha
e é seguido pelas suas notas.

jose 10 15 20 30 40
pedro 23 16 19 22
suzana 8 22 17 14 32 17 24 21 2 9 11 17
gisela 12 28 21 45 26 10
joao 14 32 25 16 89

Usando o arquivo texto notas_estudantes.txt escreva um programa que
imprime o nome dos alunos que têm mais de seis notas.

Usando o arquivo texto notas_estudantes.txt escreva um programa que
calcula a média das notas de cada estudante e imprime o nome e a média
de cada estudante.

Usando o arquivo texto notas_estudantes.dat escreva um programa que
calcula a nota mínima e máxima de cada estudante e imprima o nome de
cada aluno junto com a sua nota máxima e mínima.


'''

def mais6Notas():
    print("=-" * 25)
    print("Alunos com 6 notas ou mais")
    print("=-" * 25)
    fp.seek(0)
    for line in fp:
        dados = line.split()
        if len(dados) > 7:
            print(dados[0])

def media():
    print("=-" * 25)
    print("Listagem de alunos com suas médias")
    print("=-" * 25)
    fp.seek(0)
    for line in fp:
        dados = line.split()
        notas = list(map(float,dados[1:]))
        media = sum(notas) / len(notas)
        print(f"Aluno: {dados[0]} - Média: {media:.2f}")

def maiorMenorNota():
    print("-=" * 25)
    print("Maior e menor nota de cada aluno".center(50))
    print("-=" * 25)
    fp.seek(0)
    for aluno in fp:
        dados = aluno.split()
        notas = list(map(float, dados[1:]))
        print(f"{dados[0]}\t\tMaior: {max(notas):4.1f} - Menor: {min(notas):4.1f}")

try:
    fp = open("notas_estudantes.txt",'r')
    mais6Notas()
    media()
    maiorMenorNota()
    fp.close()
except:
    print("ERRO")