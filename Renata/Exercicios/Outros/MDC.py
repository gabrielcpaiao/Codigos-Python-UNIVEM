#iTALO MDC
#Algoritmo de Euclides para MDC
a, b = map(int, input(">> ").split())
a, b = max(a, b), min(a, b)
while b: a, b = b, a % b
print(a)