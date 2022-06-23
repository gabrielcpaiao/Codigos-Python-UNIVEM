#Gabriel Costa Paião RA: 618764 (UNIVEM 2021 Ciência da computação. 1º ano. 2º semestre)

def DNA():
    while True:
        dnarna = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U',
        }
        letrasDNA = "GCTA"
        dna = input("Digite uma sequência de DNA: ").upper()
        for i in dna:
            if i not in letrasDNA:
                print("DNA inválido. Pode conter apenas as letras 'GCTA'")
                letras = True
                break
            else:
                letras = False
        if len(dna) % 3 != 0:
            print("Sequência inválida. Deve haver uma quantidade de nucleotídeos multiplos de 3.")
            qtdeLetra = True
        else:
            qtdeLetra = False
        listaRNA = ""
        for i in dna:
            listaRNA += dnarna[i]
        global lista_RNA
        lista_RNA = listaRNA
        if not (letras) and not (qtdeLetra):
            return print(f"O RNA correspondente ao DNA escrito é: {listaRNA}")
            break

def RNA():
    aminoacidos = {
        'UAU': 'Ile',
        'UGU': 'Thr',
        'UUG': 'Asn',
        'UCG': 'Ser',
        'GUG': 'His',
        'GCU': 'Arg',
        'CAU': 'Val',
        'UGA': '',
        'UAA': '',
        'UAG': '',
    }
    listaAminoacido = ""
    for i in range(0,len(lista_RNA),3):
        if i == 0:
            listaAminoacido += aminoacidos[lista_RNA[i:i+3]]
        elif i == (len(lista_RNA)-3):
            listaAminoacido += aminoacidos[lista_RNA[i:i + 3]]
        else:
            listaAminoacido += "-" + aminoacidos[lista_RNA[i:i + 3]]
    return print(f"Polipeptídeo: {listaAminoacido}")

DNA()
RNA()