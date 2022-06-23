tabela = { "Alface": 3.20,
           "Batata": 4.25,
           "Tomate": 5.30,
           "Feijão": 4.50}
print(tabela)


for produto in tabela: #somente as chaves
    print(produto)

for produto in tabela.keys(): #somente as chaves
    print(produto)

for preco in tabela.values(): #somente os valores
    print(preco)

print("Preços dos Produtos")
for produto, preco in tabela.items(): #chaves e valores
    print("="*25)
    print(f"Produto: {produto}".center(25))
    print(f"Preço R$ {preco:.2f}".center(25))
