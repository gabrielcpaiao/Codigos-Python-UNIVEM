def jogar():
    print("*******************")
    print("***Jogo da Forca***")
    print("*******************\n")

    palavra_secreta = 'banana'.upper() #a palavra secreta ficará com todas as letras maiúscula
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0
    letras_acertadas_str = ''

    print(letras_acertadas)

    while (not enforcou and not acertou):           # enquanto não enforcou e não acertou continua no 'while'
        chute = input("Qual letra?")                # usuário insere uma letra para verificar se a letra está contida na palavra secreta
        chute = chute.strip().upper()               # a letra do chute será maiuscula e já tratado os espaços antes ou depois da letra


        if(chute in palavra_secreta):               # se a letra (chute) está contida na palavra secreta, entra no 'if'
            index = 0                               # variável para mostrar a posição da letra contida na palavra secreta
            for letra in palavra_secreta:           # iteração para rodar todas as letras da palavra secreta
                if(letra == chute):                 # se a letra da iteração for igual ao do chute, será incluída na lista letras acertadas no indíce relativo a iteração
                    letras_acertadas[index] = letra
                index += 1

        else: # incrementa se o jogador chutar uma letra que não tem na palavra secreta
            erros += 1

        enforcou = (erros ==  len(palavra_secreta)) # quando a quantidade de erros for igual a largura da palavra secreta o usuário perde o jogo (enforca-se)
        print(letras_acertadas)

        letras_acertadas_str = ''.join(letras_acertadas) #transforma a lista (letras acertadas) em uma string (letras_acertadas_str)

        if letras_acertadas_str.upper() == palavra_secreta: #compara se é igual
            acertou = True
            print("Voce acertou!")

        if (enforcou):
            print("Você perdeu! A palavra secreta é {}".format(palavra_secreta))

    print("Fim do jogo")

if (__name__ == '__main__'):
    jogar()