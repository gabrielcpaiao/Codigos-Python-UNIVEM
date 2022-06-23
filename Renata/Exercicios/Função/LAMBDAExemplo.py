from functools import reduce
#LAMBDA
valores = [10, 4, -1, 3, 5, -9, -11]
print("Números de entrada: ",valores)
print ("Números positivos: ",list(filter(lambda x: x > 0, valores)))

valores = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, valores)
print("Números de entrada: ",valores)
print ("usando lambda - Soma = ",soma)

minha_lista = [2, 4, 5, 2]
produto_total = reduce(lambda x, y: x * y, minha_lista)
print("Números de entrada: ",minha_lista)
print("Produto = ",produto_total)

'''
1. reduce recebe como argumento de função aplicada a função mult (ou a lambda, no segundo caso)
2. reduce recebe como iterável a lista minha_lista
3. reduce considera como x e y, respectivamente, os dois primeiros elementos de minha_lista: 2 e 4
4. reduce aplica a x e y a função mult, que multiplica um pelo outro: em 2 * 4, o resultado é 8.
5. O resultado da aplicação da função (nosso 8) passa a ser x, e o próximo elemento não processado (5, terceiro elemento da nossa lista) passa a ser y
6. A função mult é aplicada a x e y: 8 * 5 retorna 40, e esse valor retornado passa a ser nosso novo x
7. A função mult é aplicada pela última vez ao x e o último elemento da nossa lista, 2. 40 * 2 nos retorna 80
8. Como não há mais elementos em que aplicar a função, reduce nos retorna o resultado final: 80, como esperado.
'''