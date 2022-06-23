'''DNA: ACGT
RNA: ACGU
G -> C
C -> G
T -> A
A -> U
Final UGA, UAA e UAG.
'''
import re

novoDNA = ''
pol = ''
dnaRna = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

rnaAmi = {
    'UAU': 'Ile',
    'UGU': 'Thr',
    'UUG': 'Asn',
    'UCG': 'Ser',
    'GUG': 'His',
    'GCU': 'Arg',
    'CAU': 'Val',
}

while True:
    validaLetra = True
    validaNumeroDoDNA = True
    letrasDNA = "GCTA"
    DNA = input("Digite uma sequência de DNA: ").upper()
    for i in DNA:
        if i not in letrasDNA:
            print("DNA inválido. Pode conter apenas 'GCTA'")
        else:
            validaLetra = False
    if len(DNA) % 3 != 0:
        print(
            "Sequência inválida. Deve haver uma quantidade de nucleotídeos multiplos de 3.")
    else:
        validaNumeroDoDNA = False
        for i in range(len(DNA)):
            if any(DNA[i] in key for key in dnaRna):
                novoDNA += dnaRna[DNA[i]]
        dnas = re.split("(\S{3})", novoDNA)
        dnas = list(filter(None, dnas))

        for i in range(len(dnas)):
            if any(dnas[i] in key for key in rnaAmi):
                pol += rnaAmi[dnas[i]] + '-'

        newpol = pol[:-1]
        print('RNA => ', novoDNA)
        print('Códons RNA => ', dnas)
        print('Polipeptídeo => ', newpol)
    if not (validaLetra and validaNumeroDoDNA):
        break