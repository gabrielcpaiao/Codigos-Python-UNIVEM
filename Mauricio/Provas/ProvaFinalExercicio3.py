#Gabriel Costa Paião (RA:618764). Ciência da Computação. UNIVEM. 1º ano e 1º etapa, Noturno.
#Prova Final --> Exercício (3)
palavra = input("Digite uma palavra em português: ").lower()
copia_palavra = palavra
vogais = ["a", "e", "i", "o", "u"]

A = palavra.count("a")
E = palavra.count("e")
I = palavra.count("i")
O = palavra.count("o")
U = palavra.count("u")

X = A+E+I+O+U

#Caso não tenha vogal na palavra:
tem_vogal = False
for i in range(len(vogais)):
    if vogais[i] in palavra:
        tem_vogal = True
if not tem_vogal:
    print(f"Palavra = ({palavra}) → Não há tradução!")

#Caso a primeira letra seja vogal:
primeira_letra = palavra[0]
terminacao = "ia"
if primeira_letra in vogais:
    palavra += terminacao
    print(f"Palavra = ({copia_palavra}) → Dialeto = ({palavra})")
elif primeira_letra not in vogais and X > 0:
    #Caso em que a primeira letra não é vogal mas exista vogal na palavra:
    dialeto = ""
    terminacao = "ia"
    posicao = 1
    for j in range(len(palavra)):
        if palavra[j] not in vogais:
            dialeto += palavra[j]
            posicao = j
        else:
            break
    resultado = palavra[posicao+1:]+dialeto+terminacao
    print(f"Palavra = ({copia_palavra}) → Dialeto = ({resultado})")