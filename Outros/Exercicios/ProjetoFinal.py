import requests as r
url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
print(resp.status_code)
raw_data = resp.json()
print(raw_data[0])
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])
print((final_data))

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

print(final_data)

import datetime as dt
print(dt.time(12, 6, 21, 7), 'Hora:minuto:segundo.microsegundo')
print('----')
print(dt.date(2020, 7, 25), 'Ano-mês-dia')
print('----')
print(dt.datetime(2020, 7, 25, 12, 6, 21, 7), 'Ano-mês-dia Hora:minuto:segundo.microsegundo')

natal = dt.date(2020, 12, 25)
reveillon = dt.date(2021, 1, 1)
print(reveillon-natal)
print((reveillon-natal).days)
print((reveillon-natal).seconds)
print((reveillon-natal).microseconds)

import csv
with open("brasil_covid.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1,len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

print(final_data)

def get_datasets(y, labels):
    if type(y[0]) == list:
        dataset = []
        for i  in range(len(y)):
            dataset.append({'label': labels[i], 'data': y[i]})
        return dataset
    else:
        return [{'label': labels[0], 'data': y}]

def set_tittle(tittle=''):
    if tittle != '':
        display = 'true'
    else:
        display = 'false'
    return {'title': tittle, 'display': display}

def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_datasets(y,labels)
    options = set_tittle(title)
    chart  = {'type': kind, 'data': {'labels': x, 'datasets': datasets}, 'options': options}
