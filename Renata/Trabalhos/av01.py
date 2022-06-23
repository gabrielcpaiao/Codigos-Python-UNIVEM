#Gabriel Costa Paião (RA: 61876-4) Ciência da Computação UNIVEM (1º ano 2º etapa, Noturno)

nomeCompleto = input("Digite um nome completo: ").lower()
nomeCompleto = nomeCompleto.split()

pronomes = ["da", "de", "do", "dos"]

for i in range(len(nomeCompleto)):
    if nomeCompleto[i] not in pronomes:
        nomeCompleto[i] = nomeCompleto[i].capitalize()

nomeCompleto = " ".join(nomeCompleto)
print()
print(f"O nome com todas as iniciais maiúsculas fica: \n{nomeCompleto}")