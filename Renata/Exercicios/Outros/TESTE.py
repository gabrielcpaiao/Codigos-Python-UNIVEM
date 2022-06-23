'''print("Digite três valores diferentes: ")
a = int(input())
b = int(input())
c = int(input())
if (a>c):
    a,c = c,a
if (a>b):
    a,b = b,a
if (b>c):
    b,c = c,b
print(f"Os números em ordem crescente são: {a}, {b} e {c}")'''


'''from random import sample
a= sorted(sample(range(1,61),6))
print(a)
'''


'''
M = [0] * 2
for i in range(2):
    M[i] = [0] * 3
    print(f"Linha {i}")
    for j in range(3):
        M[i][j] = int(input(f"[{i}][{j}] >> "))

print(M)

for i in range(2):
    for j in range(3):
        print(M[i][j],end=" ")
    print()
'''


'''
from random import randint

M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        M[i][j] = randint(1,99)
        print(f"{M[i][j]:02}",end=" ")
    print()
'''



'''
from random import randint

M = []
for i in range(5):
    M.append([])
    for j in range(5):
        M[i].append(randint(1,99))
        print(f"{M[i][j]:02}",end=" ")
    print()
'''



'''
M=[[1,2,3],[4,5,6]]
for i in range(2):
    for j in range(3):
        print(f"[{M[i][j]:^3}] ",end='')
    print()
'''


'''
from random import randint

M = []
for i in range(5):
    M.append([])
    for j in range(5):
        M[i].append(randint(1,99))
    print(*M[i])

#acessando posições da matriz
print(M[0][1]) #imprimir o valor na linha 0, coluna 1
print(M[0]) #imprimir a primeira linha
print(*M[0]) #imprimir a primeira linha, sem [] e sem vírgulas
'''




'''
#Gabriel Costa Paião (RA: 61876-4). Ciência da computação 1ºano, 1º etapa.
from random import randint
m = [0]*10
for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        m[i][j] = randint(0,9)
print("A matriz gerada é: ")
print()
for i in range(10):
    for j in range(10):
        print(f"{m[i][j]:^2}", end=" ")
    print()
print()
print("Digite um número de três algorismos: ")
while True:
    n = int(input())
    if n<100 or n>1000:
        print("Digite um número válido.")
    else:
        break

c = n//100
d = (n%100)//10
u = n%10

for i in range(10):
    for j in range(10):
        if
def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)

a = "a"
if a.isupper():
    print("Sim")

lista = [1,2,3,4]
print(f"alo {''.join(lista[-1::-1])}")


a = []
for i in range(5):
    n = int(input())
    a.append(int(n))
l = 0
m = 0
o = 0
p = 0
for j in range(5):
    if a[j] % 2 == 0:
        l += 1
    if a[j] % 2 == 1:
        m += 1
    if a[j] > 0:
        o += 1
    if a[j] < 0:
        p += 1
print(l, "valor(es) par(es)")
print(m, "valor(es) impar(es)")
print(o, "valor(es) positivo(s)")
print(p, "valor(es) negativo(s)")'''

#Importar bibliotecas
from random import randint
import time
import urllib.request

#Configurar a API do thingSpeak
#APIJay
myAPI = '4CND1AJ91ZCEU4L8'
#URL base do canal
baseURL = "https://api.thingspeak.com/update?api_key=" +myAPI

#Teste da URL
print(baseURL)

def gerar_dados():
  temp = randint(0,50)
  umd = randint(0,100)
  return temp, umd

#Teste de envio de dados do canal
temp, umd = gerar_dados()
print(baseURL+'&field1=%s&field2=%s' % (temp, umd))

while True:
  print("Inicializando...")
  try:
    print("Coletando dados...")
    temp, umd = gerar_dados()
    print("Temperatura: ", temp,"Umidade: ", umd)
    conn = urllib.request.urlopen(baseURL + '&field1=%s&field2=%s' % (temp, umd))
    conn.close()
    time.sleep(60)
  except:
    break