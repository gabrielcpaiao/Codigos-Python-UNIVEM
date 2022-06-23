contato = {}

def cadastro():
    nome = input("Nome -> ").upper()
    email = input("e-mail -> ").lower()
    contato[nome] = email

def consultaPorNome():
    nome = input("Nome -> ").upper()
    if nome in contato:
        print('e-mail: ',contato[nome])
    else:
        print(f"'{nome}' não encontrado")

def consultaPorEmail():
    email = input("e-mail -> ").lower()
    if email in contato.values():
       i = list(contato.values()).index(email)
       print("Nome ->",list(contato.keys())[i])
    else:
        print(f"'{email}' não encontrado")

def listagem():
    for n, e in contato.items():
        print(f"Nome: {n} ✉: {e}")

while True:
    op = int(input("1. Cadastar"
                   "\n2. Consultar por nome"
                   "\n3. Consultar por e-mail"
                   "\n4. Listar"
                   "\n5. Encerrar"
                   "\nOpção -> "))
    if op == 5:
        break
    elif op == 1:
        cadastro()
    elif op == 2:
        consultaPorNome()
    elif op == 3:
        consultaPorEmail()
    elif op == 4:
        listagem()
    else:
        print("Opção inválida")