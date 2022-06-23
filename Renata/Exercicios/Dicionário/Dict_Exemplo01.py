tabela = { "Alface": 3.20,
           "Batata": 3.50,
           "Tomate": 5.30,
           "Feijão": 4.50}
print(tabela)

print(tabela["Alface"])
tabela["Tomate"] = 5.50
tabela["Cebola"] = 4.68
print(tabela)

if "Manga" in tabela:
    print(tabela["Manga"])
else:
    print("Não há Manga")

print(tabela.get("Alface","Não encontrado"))

print(tabela.items())
print(tabela.keys())
print(tabela.values())

del tabela["Alface"]
print(tabela.pop("Manga","Não encontrada"))
print(tabela)

