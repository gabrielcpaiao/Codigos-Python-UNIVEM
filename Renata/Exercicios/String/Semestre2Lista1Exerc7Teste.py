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