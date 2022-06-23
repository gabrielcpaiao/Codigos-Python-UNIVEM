a = int(input("Informe um valor >> "))
b = int(input("Informe outro valor >> "))
print(f"Valores informados: {a} - {b}")
x = a
a = b
b = x
# em python é possível fazer a troca assim:
#a, b = b, a
print(f"Valores trocados:   {a} - {b}")