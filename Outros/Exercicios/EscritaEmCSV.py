import csv
with open("users.csv", "w", encoding="utf-8", newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Gabriel', 'Paião', 'gabrielpaiao@email.com', 'Masculino'])
with open('users.csv', 'r', encoding="utf-8", newline='') as arquivo_users:
    print(arquivo_users.read(), end="")