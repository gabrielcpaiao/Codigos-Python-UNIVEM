tabela = { "Alface": 3.20,
           "Batata": 3.20,
           "Tomate": 5.30,
           "Feijão": 4.50}

def busca(produto):
    if produto in tabela:
        return tabela[produto]
    return "Produto não cadastrado"

def reverse_busca(p):
    l = []
    for k in tabela:
        if tabela[k] == p:
            l.append(k)
    if len(l) > 0:
        return l
    return "Preço não encontrado"

print("O preço do feijão é",busca("Feijão"))
print("Os produtos que custam R$ 3.20 são: ",reverse_busca(3.20))
