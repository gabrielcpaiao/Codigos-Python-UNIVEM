import random
valor_apostado = float(input("O valor da aposta é de: "))
num_apostado = int(input("Digite um valor de 1 a 36: "))
num_aleatorio = random.randint(1, 37)
print("O valor sorteado foi: ", num_aleatorio)
if num_apostado not in range(0,36):
    print("Este valor não está entre o intervalo solicitado")
elif num_apostado==num_aleatorio:
    print(f"O valor ganho é de :{5*valor_apostado}")
elif (((num_apostado in range(1,12)) and (num_aleatorio in range(1,12))) or ((num_apostado in range(13,24)) and (num_aleatorio in range(13,24))) or ((num_apostado in range(25,36)) and (num_aleatorio in range(25,36)))):
    print(f"O valor ganho é de :{3 * valor_apostado}")
elif (((num_apostado%2==0) and (num_aleatorio%2==0)) or ((num_apostado%2!=0) and (num_aleatorio%2!=0))):
    print(f"O valor ganho é de :{2 * valor_apostado}")
else:
    print("O apostador perdeu o valor apostado")