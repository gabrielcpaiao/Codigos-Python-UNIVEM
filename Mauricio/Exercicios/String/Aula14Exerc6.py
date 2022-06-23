#ler um e-mail e mostras seu domínio (entre o @ e o .)
print("Digite um e-mail: ")
email = input()
dominio = ""
inicio = email.find('@')+1
fim  = email[inicio: ].find('.')
dominio += email[inicio: inicio+fim]
print("Domínio = ", dominio)

'''
email = input("Digite um email:\n")
dominio = email.find("@")
emaileditado = email[dominio:len(email)]
dominio = emaileditado[1:emaileditado.find(".")]
print(f"Domínio:\n{dominio}")

'''

'''
email = str(input('digite o email'))
email = email.strip()

k ="@"
k1 = 0
k2 = '.'
k3 = 0
print(email)
for i in range(len(email)):
    if email[i] == k:
        k1 = i
    if i > k1 and email[i] == k2:
        k3 = i
print(email[k1+1:k3])
'''