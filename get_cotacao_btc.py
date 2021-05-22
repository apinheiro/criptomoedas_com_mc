import requests, json, os, configparser
from tqdm import tqdm
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')
start = datetime.fromisoformat(config['btc']['start'][:-2])

end = datetime(2021,5,22,0,0,0)
url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?limit=50000&period_id=1HRS&time_start={}&time_end={}'.format(start.strftime("%Y-%m-%dT%H:%M:%S"),end.strftime("%Y-%m-%dT%H:%M:%S"))

# Código usando o id.uff.br
#headers = {'X-CoinAPI-Key' : '14C54900-249E-4D61-BD8F-53B540EF49C9'}
#
# Código usando digital3i
headers = {'X-CoinAPI-Key':'70AA6AE1-90B0-481E-B9CF-998A3F592705'}
print('Iniciando Consulta')
response = requests.get(url, headers=headers)
print('Convertendo Json')
trades = json.loads(response.text)

print('Iniciando a gravação')
tq = tqdm(total=len(trades))
with open(os.path.join('dataset','trades_btc_usd.csv'),'a') as c:
    anterior = float(config['btc']['anterior'])
    for t in trades:
        atual = float(t['rate_close'])
        c.writelines(f"{t['time_period_end']};{t['rate_close']};{1 if atual > anterior else 0};{1 if atual <= anterior else 0}\n")
        anterior = atual
        datafim = t['time_period_end']
        tq.update(1)

config['btc']['start'] = datafim
config['btc']['anterior'] = str(anterior)
with open('config.ini','w') as file:
    config.write(file)