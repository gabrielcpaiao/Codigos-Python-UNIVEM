'''
Faça um programa em Python para controlar uma
agenda telefônica, criando um dicionário,
armazenando o nome e o telefone,
programando as seguintes funções:
–	Cadastrar um contato
–	Consultar um contato
–	Listar todos os contatos
'''
def faixa(texto):
    texto = texto.upper()
    print("=" * 50)
    print(f"{' '.join(texto)}".center(50))
    print("=" * 50)

def novo():
    faixa("Novo contato")
    nome = input("Informe o nome -> ").upper()
    telefone = input("Telefone -> ")
    agenda[nome] = telefone

def consulta():
    faixa("consulta")
    nome = input("Informe o nome para consulta -> ").upper()
    if nome in agenda:
        print("Contato encontrado - Telefone -> ",agenda[nome])
    else:
        print("Contato não encontrado")

def listagem():
    faixa("listagem")
    for nome, fone in agenda.items():
        print(f"Contato -> {nome} - {fone}")

agenda = {}

while True:
    faixa("Agenda Telefônica")
    op = int(input("1. Novo contato"
                   "\n2. Consultar"
                   "\n3. Listar"
                   "\n4. Sair"
                   "\nOpção -> "))
    if op == 4:
        break
    elif op == 1:
        novo()
    elif op == 2:
        consulta()
    elif op ==3:
        listagem()
    else:
        print("Opção inválida!!")