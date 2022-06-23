'''
Faça um programa que receba dois arquivos do usuário, e
crie um terceiro arquivo com conteúdo dos dois primeiros
juntos (o conteúdo do primeiro seguido do conteúdo do segundo).
'''

try:
    arq1 = open(input("Informe o nome do 1º arquivo -> "),'r',encoding='utf-8')
    arq2 = open(input("Informe o nome do 2º arquivo -> "),'r',encoding='utf-8')
    arq3 = open("a3.txt",'w+',encoding='utf-8')
    arq3.write(arq1.read()+'\n'+arq2.read())
    arq3.seek(0)
    print(arq3.read())
    arq1.close()
    arq2.close()
    arq3.close()
except:
    print("Algum arquivo inexistente")