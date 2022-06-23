from random import randint
from  time import sleep
from operator import itemgetter
jogo = {'J1': randint(1,6),
        'J2': randint(1,6),
        'J3': randint(1,6),
        'J4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
print("-=" * 30)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)