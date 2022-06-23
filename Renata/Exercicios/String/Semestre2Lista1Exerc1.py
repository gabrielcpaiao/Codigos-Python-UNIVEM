'''
Faça um programa que conte o número de 1’s que aparecem em uma string. Exemplo:
“0011001” -> 3.
'''

frase = input("Digite uma sequência de números: ")
x = frase.count("1")
print(f"Existe {x} 1's nesta sequência.")