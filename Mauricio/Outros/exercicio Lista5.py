print("Digite o primeiro valor:")
a = int(input())
print("Digite o segundo valor: ")
b = int(input())
print("Digite o terceiro valor: ")
c = int(input())
if a>b and a>c:
    print("O maior valor é o primeiro")
elif b>c:
    print("O maior valor é o segundo")
else:
    print("O maior valor é o terceiro")