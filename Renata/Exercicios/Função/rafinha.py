'''
Duas funções p elevar ao quadrado e cubo aplicar simultaneamente a lista
'''
def quadrado(a):
    x = a**2
    return x

def cubo(b):
    y = b**3
    return y

lista = [0,1,2,3,4]

resultado = [0,0]

for i in lista:
    resultado[0] = quadrado(i)
    resultado[1] = cubo(i)
    print(resultado)