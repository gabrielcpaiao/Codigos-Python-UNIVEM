#ler um nome e inserir em um e-mail (@univem.edu.br)
print("Digite um nome: ")
n = input()
n = n.split()
email = "".join(n)+"@univem.edu.br"

print(n)