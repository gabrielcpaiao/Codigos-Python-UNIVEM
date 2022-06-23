'''
Faça um programa em Python que leia o nome e
duas notas de N alunos e armazene em um arquivo texto.
Após a leitura faça a impressão de todos os alunos inseridos.
'''

def cadastrar():
    fp = open("notas.txt","a")
    nome = input("Nome -> ")
    n1 = input("Nota 1 -> ")
    n2 = input("Nota 2 -> ")
    fp.write(f"{nome};{n1};{n2}\n")
    fp.close()

def listar():
    try:
        fp = open("notas.txt",'r')
        for aluno in fp:
            dados = aluno.split(";")
            notas = list(map(float,dados[1:]))
            media = sum(notas)/len(notas)
            print(f"Aluno: {dados[0]}"
                  f"\nNota 1: {notas[0]:.2f}"
                  f"\nNota 2: {notas[1]:.2f}"
                  f"\nMédia: {media:.2f}")
            print("-"*50)
    except:
        print("Arquivo não existe")
    finally:
        fp.close()

while True:
    op = int(input("1. Cadastrar\n2. Listar\n3. Sair\nOpção -> "))
    if op == 3:
        break
    elif op == 1:
        cadastrar()
    elif op == 2:
        listar()
    else:
        print("Opção inválida")