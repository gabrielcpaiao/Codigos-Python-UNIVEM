gab = [0]*10
for i in range(10):
    gab[i] = input()
candidato = [0]*10
soma = 0
for i in range(10):
    candidato[i] = input()
    if (gab[i] == candidato[i]):
        soma +=1
print(f"A nota deste aluno é: {soma}")