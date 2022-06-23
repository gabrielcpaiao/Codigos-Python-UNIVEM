'''
Faça um programa que leia um número indeterminado
de valores,correspondentes a notas, fazendo
a entrada usando split() e convertendo a lista
para float.
Após esta entrada de dados, faça:
Exiba todos os valores na ordem em que
foram informados, um ao lado do outro;
Mostre a quantidade de valores que foram lidos;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Remova a menor nota e exiba a lista novamente;
Calcule e mostre quantas notas são iguais a 10;
Remova a primeira nota;
Remova a última nota;
Exiba a lista novamente;
'''
notas = input("Entre com as notas -> ").split()
print(notas)
for i in range(len(notas)):
    notas[i] = float(notas[i])
print(notas)
print(f"Quantidade de valores que foram lidos -> {len(notas)}")
print(f"Soma dos valores -> {sum(notas)}")
print(f"Média dos valores -> {sum(notas)/len(notas):.2f}")
notas.remove(min(notas))
print(notas)
print(f"Notas iguais a 10 -> {notas.count(10)}")
notas.pop(0)
notas.pop()
print(notas)
