#No exercício 3 pede pra eu digitar o valor do angulo que o avião decola. Por isso, deve haver duas validações para que o avião decole (1º: a altura de segurança tem que ser maior que o tamanho do predio e o angulo que eu digitar, convertido em tangente, deve ser maior qe a tangente de "Y/X")
import math
X = float(input("Digite a distância entre o aeroporto e o prédio: "))
Y = float(input("Digite o tamanho do prédio: "))
Z = float(input("Digite a altura de segurança do voo: "))
W = float(input("Digite o ângulo entre o avião e o solo em graus: "))

w = math.tan(math.radians(W))
teste2 = math.tan(math.radians(Y/X))


if ((W - Y >0) and w>teste2):
    print("O avião pode decolar")
else:
    print("O avião não pode decolar")