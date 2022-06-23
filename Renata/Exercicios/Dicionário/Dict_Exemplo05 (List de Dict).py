galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input("Nome: ")
    pessoa['sexo'] = input("Sexo: [F/M] ").upper()[0]
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resp = input("Quer continuar? [S/N] ").upper()[0]
    if resp == 'N':
        break
print("-=" * 30)
print(galera)
print("a) Ao todos temos {} pessoas cadastradas".format(len(galera)))
media = soma / len(galera)
print("b) A média de idade é de {:.2f} anos".format(media))
print("c) Mulheres cadastradas")
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'],end=" ")
print()
print("d) Lista das pessoas que estão acima da média")
for p in galera:
    if p['idade'] >= media:
        print("   ",end="")
        for k, v in p.items():
            print("{} = {}; ".format(k,v), end="")
        print()
print("<<ENCERRADO>>")