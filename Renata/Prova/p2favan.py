#Coletar, transmitir, armazenar, analisar os dados e reagir/controlar.

from random import randint
#Para usar URL
import urllib.request

#Configurando a API do thingSpeak
#Usando a chave de API
chave = 'AR0H2VQC2679JBOR'  #Serve para enviar dados
#URL base do canal
#Para mandar dados, pegar a Write a Channel Feed (pegar só até a parte key=) e contatenar na base.
linkurl = "https://api.thingspeak.com/update?api_key="+chave
#Ao clicar no link acima, se aparecer 1 é porque encontrou o canal no thingSpeak

#De 5 mm a 60 mm em uma hora, a chuva é moderada.

def dados():
    chuva = randint(5,100)
    return chuva

try:
    chuva = dados()
    print("Choveu", chuva,"mm!")
    #Conectar com o thingSpeak usando a biblioteca urllib para jogar os dados na nuvem
    conexao = urllib.request.urlopen(linkurl + '&field1=%s' % (chuva))
    #Fechando a conexão
    conexao.close()
except:
    print("Algo deu errado. Verifique todas as possibilidades.")