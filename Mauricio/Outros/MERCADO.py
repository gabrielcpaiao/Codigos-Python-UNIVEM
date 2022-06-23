'''
Você dispoem de um valor em dinheiro e deve comprar a maior quantidade possível de produtos essenciais. Caso de pra comprar todos, levar
mais produtos que não sejam essenciais.

L = ["arroz","feijão","cerveja","ovos","sabonete","sorvete","requeijão","chocolate","queijo","maça"]
P = [26.00,8.50,3.50,7.30,2.30,22.00,9.50,6.20,25.50,5.60]
L = []
P = []
'''

palavraChave = input("Digite a palavra chave: ").lower()
frase = input("Digite uma frase: ").lower()
qtdLinha = (len(frase)//len(palavraChave))+1
m = [0]*qtdLinha
posicao = 0
x = len(palavraChave)


for i in range(qtdLinha):
    if posicao <= len(frase):
        m[i] = frase[posicao:x]
        posicao += len(palavraChave)
        x += len(palavraChave)
        if x > len(frase):
            m[i] = frase[posicao:len(frase)]



for i in range(qtdLinha):
    for j in range(len(palavraChave)):
        print(f"{m[i][j]:^2}", end=" ")
    print()