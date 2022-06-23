#Idoso (idade >= 65)
#Ler vetor de 20 idades (entre os idosos, mostrar o mais novo e a média das idades)

vetor = []
menor = 1000
cont = 0
soma = 0
for i in range(20):
    while True:
        idade = int(input("Digite uma idade: "))
        if 0 <= idade <= 110:
            break
        else:
            print("Digite uma idade válida!")
    vetor.append(idade)
    if 65 <= idade < menor:
        menor = idade
    if idade >= 65:
        soma += idade
        cont += 1
print("As idades digitadas são:")
print(vetor)
print()
print(f"Dentre as idade digitadas o(a) idoso(a) mais novo possui {menor} anos e a média das idades dos idosos nesta lista é {soma//cont} anos.")