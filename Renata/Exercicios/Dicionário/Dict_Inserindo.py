tabela = dict() #ou {}
while True:
    produto = input("Informe o produto, fim para encerrar: ")
    if produto == "fim":
        break
    if produto in tabela:
        print("Produto já cadastrado")
    else:
        preco = float(input("Informe o preço: "))
        tabela[produto] = preco # inserir em dicionário
print(tabela)