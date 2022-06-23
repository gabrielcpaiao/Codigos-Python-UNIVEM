#Calcular a altura do avião.

import math
altura = 2000 * math.sin(math.radians(20))
print(altura)

##No exercício 3 pede pra mim digitar o valor do angulo que o avião decola. Por isso, deve haver duas validações para que o avião decole (1º: a altura de segurança tem que ser maior que o tamanho do predio e o angulo que eu digitar, convertido em tangente, deve ser maior qe a tangente de "Y/X")