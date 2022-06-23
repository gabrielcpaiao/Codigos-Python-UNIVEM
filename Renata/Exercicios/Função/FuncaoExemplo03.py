#Variáveis globais e locais

def troca():
    global a
    a = 5
    print(f"Dentro da função {a}")


a = 10
print(f"Antes da chamada da função {a}")
troca()
print(f"Após a chamda da função {a}")