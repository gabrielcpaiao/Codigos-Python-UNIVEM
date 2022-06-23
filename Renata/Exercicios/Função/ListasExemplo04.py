from random import randint
L = []
for i in range(5):
    L.append(randint(1,50))
print(L)
print(f"Maior valor da lista -> {max(L)}")
print(f"Menor valor da lista -> {min(L)}")
print(f"Soma dos valores da lista -> {sum(L)}")
print(f"Média dos valores da lista -> {sum(L)/len(L)}")