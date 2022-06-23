from random import randint
import time
#Para usar as URL
import urllib.request

#Configurando a API do thingSpeak
#Usando a chave de API
myAPI = 'AR0H2VQC2679JBOR'  #Serve para enviar dados
#URL base do canal
#Para mandar dados, pegar a Write a Channel Feed (pegar só até a parte key=) e contatenar na base.
baseURL = "https://api.thingspeak.com/update?api_key="+myAPI
#Ao clicar no link acima, se aparecer 1 é porque encontrou o canal no thingSpeak

def gerarDados():
    temperatura = randint(0,50)
    return temperatura

#Teste para ver se consegue enviar dados para o canal
temperatura = gerarDados()
print(baseURL+'&field1=%s' % (temperatura)) #Aloca no campo da temperatura
#Caso o retorno desse link for 2, quer dizer que der certo

while True:
    try:
        temperatura = gerarDados()
        print("Temperatura: ", temperatura)
        #Conectar com o thingSpeak usando a biblioteca urllib para jogar os dados na nuvem
        conn = urllib.request.urlopen(baseURL + '&field1=%s' % (temperatura))
        #Fechando a conexão
        conn.close()
        #sleep(60)
    except:
        break