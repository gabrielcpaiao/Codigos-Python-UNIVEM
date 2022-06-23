#inverter a mensagem. Avançar o caracter para o terceiro a sua frente( a vira d, b vira e) (x=a, y=b, z=c)
#chr(ord('c')+1) produz "d"
#printar a mensagem criptografada no final

print("Digite uma mensagem: ")
msg = input().lower()
aux = ""
for i in range(len(msg)):
    if msg[i] == 'x':
        aux += 'a'
    elif msg[i] == 'y':
        aux += 'b'
    elif msg[i] == 'z':
        aux += 'c'
    else:
        aux += chr(ord(msg[i]) + 3)
print(aux)