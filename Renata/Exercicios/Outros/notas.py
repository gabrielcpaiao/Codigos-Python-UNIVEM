#A nota ﬁnal de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente,
# a um trabalho de laboratório, a uma avaliação semestral e a um exame ﬁnal. A média das três notas mencionadas anteri
# ormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resulta
# do, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado.
# Faça todas as veriﬁcacões
#trabalho 2
#avaliação 3
#exame 5
#reprovado (0~2,9)
#recuperação (3~4,9_)
#aprovado

print("Digite a nota do trabalho obtida pelo aluno:")
trabalho = float(input())
print("Digite a nota da avaliação obtida pelo aluno:")
avaliação = float(input())
print("Digite a nota do exame obtida pelo aluno:")
exame = float(input())
media = (trabalho*2 + avaliação*3 + exame*5)/(10)
if (trabalho<0 or trabalho>10 or avaliação<0 or avaliação>10 or exame<0 or exame>10):
    print("Vefirique! Alguma nota está incorreta.")
elif 0<=media<3:
    print("Aluno reprovado")
elif 3<=media<5:
    print("Aluno de recuperação")
else:
    print("Aluno aprovado")
#professora:
