'''
Faça um programa no qual o usuário informa o nome do arquivo,
e uma palavra, e retorne o número de vezes que aquela palavra
aparece no arquivo.
'''

try:
    nomeArq = input("Informe o nome do arquivo -> ")
    palavra = input("Informe a palavra de busca -> ").upper()
    fp = open(nomeArq,'r',encoding='utf-8')
    texto = fp.read().upper()
    print(f"Tem {texto.count(palavra)} '{palavra}' no texto")
    fp.close()
except FileNotFoundError:
    print("Arquivo inexistente")
except:
    print("ERRO!!")