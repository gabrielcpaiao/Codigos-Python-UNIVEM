temp0 = float('inf')
for i in range(3):
    name = input()
    temp = float(input())
    if temp<temp0:
        temp0 = temp
        name1 = name
print(f"O menor tempo foi do atleta {name1}, cujo valor foi de {temp0}")


#Professor:
'''
for i in range(11):
    tempo = int(input("Digite o tempo em segundos: "))
    if (i==0):
        menor = tempo
    elif(tempo<menor):
        menor = tempo
print("Tempo mais rápido: ", menor)
'''