while True:
    opcao = input("Digite uma opção:\n"
                  "a - Ler uma string S1\n"
                  "b - Imprimir o tamanho da string S1\n"
                  "c - Comparar a string S1 com uma nova string S2 fornecida pelo usuário e imprimir o resultado da comparação\n"
                  "d - Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da concatenação\n"
                  "e - Imprimir a string S1 de forma reversa\n"
                  "f - Contar quantas vezes um dado caractere aparece na string S1. Esse caractere desse ser informado pelo usuário\n"
                  "g - Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2. Os caracteres C1 e C2 serão lidos pelo usuário\n"
                  "h - Verificar se uma string S2 é substring de S1. A string S2 deve ser informada pelo usuário\n"
                  "i - Criar uma substring da string S1. Para isso o usuário deve informar a partir de qual posiçãodeve ser criada a substring e qual é o tamanho da substring. Imprima a substring\n"
                  "j - Imprimir quantos caracteres estão em maiúsculo: \n"
                  "x - Encerra o programa\n"
                  ": ").lower()
    if opcao == "x":
        break
    elif opcao == "a":
        S1 = input("Digite uma string: ")
    elif opcao == "b":
        print(f"O tamanho da string é: {len(S1)}")
    elif opcao == "c":
        print("Digite uma nova string (S2):\n")
        S2 = input(": ")
        if S1 > S2:
            print(f"A string S1 ({S1}) é maior que a string S2({S2}).")
        elif S2 > S1:
            print(f"A string S2 ({S2}) é maior que a string S1({S1}).")
        else:
            print("As strings possuem o mesmo tamanho.")
    elif opcao == "d":
        S2 = input("")
        S1 += S2
        print(S1)
    elif opcao == "e":
        print(S1[::-1])
    elif opcao == "f":
        caractere = input("Digite um caractere: ")[0]
        print(S1.count(caractere))
    elif opcao == "g":
        print("Digite dois caracteres:\n")
        c1 = input()[0]
        c2 = input() [0]
        print(S1.replace(c1, c2))
    elif opcao == "h":
        S2 = input("Digite uma string: ")
        if S2 in S1:
            print(f"A string S2 {S2} é substring de S1{S1}.")
        else:
            print(f"A string S2 {S2} não é substring de S1{S1}.")
    elif opcao == "i":
        tm1 = input("Digite a partir de qual posição deseja criar a substring: ")
        tm2 = input("Digite o tamanho da substring que deseja criar: ")
        S2 = S1[tm1:tm1+tm2]
        print(S2)
    elif opcao == "j":
        soma = 0
        for letra in S1:
            if letra.isupper():
                soma += 1
        print(f"Têm {soma} letras maiúsculas na string S1.")
    else:
        print("Opção inválida!")


'''
7. Faça um programa que contenha um menu com as seguintes opções: 
(a) Ler uma string S1
(b) Imprimir o tamanho da string S1; 
(c) Comparar a string S1 com uma nova string S2 fornecida pelo usuário e imprimir o resultado da comparação;
(d) Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da concatenação;
(e) Imprimir a string S1 de forma reversa; 
(f) Contar quantas vezes um dado caractere aparece na string S1. Esse caractere desse ser informado pelo usuário; 
(g) Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2. Os caracteres C1 e C2 serão lidos pelo usuário; 
(h) Verificar se uma string S2 é substring de S1. A string S2 deve ser informada pelo usuário;
(i) Criar uma substring da string S1. Para isso o usuário deve informar a partir de qual posição deve ser criada a substring e qual é o tamanho da substring. Imprima a substring.
(j) Imprimir quantos caracteres estão em maiúsculo.
'''
'''
while True:
    op = input("a. Ler"
               "\nb. Tamanho"
               "\nc. Comparação"
               "\nd. Concatenação"
               "\ne. Reversa"
               "\nf. Contagem"
               "\ng. Troca"
               "\nh. Pertencimento"
               "\ni. Substring"
               "\nj. Maiúsculo"
               "\nx. Encerrar"
               "\n\nOpção >> ").lower()[0]
    if op == 'x':
        break
    elif op == 'a':
        S1 = input()
    elif op == 'b':
        print(f"Tamanho da string >> {len(S1)}")
    elif op == 'c':
        S2 = input()
        if S1 == S2:
            print("São iguais")
        elif S1 > S2:
            print(f"{S1} é maior que {S2}")
        else:
            print(f"{S1} é menor que {S2}")
    elif op == 'd':
        S2 = input()
        S1 += S2
        print(S1)
    elif op == 'e':
        print(S1[::-1])
    elif op == 'f':
        c = input()[0]
        print(f"Tem {S1.count(c)} na string {S1}")
    elif op == 'g':
        c1 = input()[0]
        c2 = input()[0]
        print(S1.replace(c1,c2))
    elif op == 'h':
        S2 = input()
        if S2 in S1:
            print(f"{S2} é substring de {S1}")
        else:
            print(f"{S2} não é substring de {S1}")
    elif op == 'i':
        ini = int(input("início: "))
        tam = int(input("tamanho: "))
        S2 = S1[ini:ini+tam]
        print(S2)
    elif op == 'j':
        c = 0
        for letra in S1:
            if letra.isupper():
                c += 1
        print(f"Tem {c} caracteres em maiúsculo")
    else:
        print("Opção inválida!!!")
'''