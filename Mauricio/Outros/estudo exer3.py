#5 alunos. Ler 2 notas. Calcular a média e verificar se foi aprovado (média>=6). Média geral da classe e quantos aprovados e reprovados
para = 1
ap = 0
rp = 0
soma = 0
while(para<=5):
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    media = (n1 + n2)/2
    print(f"Média= {media}")
    if (media>=6):
        print("Aluno aprovado.")
        ap+=1
    else:
        print("Aluno reprovado.")
        rp +=1
    soma += media
    para += 1
print(f"A média geral da classe é de: {soma}")
print(f"O número de alunos aprovados é igual a: {ap}")
print(f"O número de alunos reprovados é igual a: {rp}")