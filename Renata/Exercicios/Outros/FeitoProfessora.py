'''
Faça um programa que gere uma matriz 5x20, onde as linhas representam as
disciplinas de um curso.
O programa deve gerar as médias dos alunos, entre 0 e 10
(pesquise a função uniform() da biblioteca random) e
mostrar o seguinte menu com as opções:
1. Imprimir a matriz toda.
2. Pedir um número do aluno (1 a 20)
    e exibir suas notas, com a informação de “Aprovado” ou “Reprovado”.
    (Média 6 para aprovação)
3. Pedir um número da disciplina (1 a 5) e exibir as notas dos alunos,
    com a média geral da turma
4. Sair
Obs.: Para arredondar as notas geradas pela função uniform(),
pesquise a função round().
'''
from random import uniform

m = []
for i in range(5):
    m.append([])
    for j in range(20):
        m[i].append(round(uniform(0,10),1))

while True:
    op = int(input("1. Imprimir notas"
                   "\n2. Notas de um aluno"
                   "\n3. Notas de uma disciplina"
                   "\n4. Sair"
                   "\nOpção >> "))
    if op == 1:
        print("="*100)
        print("Notas da turma nas 5 disciplinas")
        for i in range(5):
            for j in range(20):
                print(f"{m[i][j]:4.1f}",end=" ")
            print()
        print("=" * 100)
    elif op == 2:
        print("=" * 100)
        aluno = int(input("Informe o número do aluno [1-20] >> "))
        for i in range(5):
            print(f"Disciplina {i+1} - Nota: {m[i][aluno-1]:4.1f}", end=" ")
            if m[i][aluno-1] >= 6:
                print(">> APROVADO")
            else:
                print(">> REPROVADO")
        print("=" * 100)
    elif op == 3:
        print("=" * 100)
        disc = int(input("Informe o número da disciplina [1-5] >> "))
        media = 0
        for i in range(20):
            print(f"{m[disc-1][i]:4.1f}",end=" ")
            media += m[disc-1][i]
        media /= 20
        print(f"\nMédia da disciplina {disc} >> {media:4.1f}")
        print("=" * 100)
    elif op == 4:
        break
    else:
        print("Opção inválida!!")