'''
Faça um programa em Python que leia o nome,
a altura e o peso de N atletas e armazene em um
arquivo texto, separados por um ponto e vírgula.
Após a leitura faça a impressão de todos os nomes,
seguidos pelo valor do IMC, que é calculado por peso/altura ao quadrado.
'''

def cadastrar():
    arq = open("atletas.txt","a")
    print("Entre com os dados do atleta")
    nome = input("Nome -> ")
    altura = input("Altura -> ")
    peso = input("Peso -> ")
    arq.write(f"{nome};{altura};{peso}\n")
    arq.close()

def listar():
    try:
        arq = open("atletas.txt","r")
        for line in arq:
            a = line.split(';')
            nome = a[0]
            altura = float(a[1])
            peso = float(a[2])
            imc = peso/altura**2
            print(f"Atleta: {nome} - IMC: {imc:.2f}")
            print("-" * 50)
        arq.close()
    except:
        print("Arquivo inexistente")

while True:
    print("=" * 50)
    op = int(input("1. Cadastrar\n2. Listar\n3. Sair\nOpção -> "))
    print("=" * 50)
    if op == 3:
        break
    elif op == 1:
        cadastrar()
    elif op == 2:
        listar()
    else:
        print("Opção inválida")