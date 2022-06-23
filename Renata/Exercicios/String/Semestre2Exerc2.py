#capitalize() = coloca a primeira posição para maiúsculo e o resto pra minusculo

nome = 'gabriel'
print(nome)
print(nome.upper())
print(nome)

nome = nome.capitalize()
print(nome)

nome = str(input('digite o seu nome completo: '))

nome = nome.split(' ')

for i in range(len(nome)):
    nome[i] = nome[i].capitalize()

print(nome)