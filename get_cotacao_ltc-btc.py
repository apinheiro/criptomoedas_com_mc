import requests, json, os, configparser
from tqdm import tqdm
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')
start = datetime.fromisoformat(config['ltc']['start'][:-2])

end = datetime(2021,5,22,0,0,0)
url = 'https://rest.coinapi.io/v1/exchangerate/LTC/BTC/history?limit=50000&period_id=1HRS&time_start={}&time_end={}'.format(start.strftime("%Y-%m-%dT%H:%M:%S"),end.strftime("%Y-%m-%dT%H:%M:%S"))

# Código usando o id.uff.br
headers = {'X-CoinAPI-Key' : 'sua_api'}
#

print('Iniciando Consulta')
response = requests.get(url, headers=headers)
print('Convertendo Json')
trades = json.loads(response.text)

print('Iniciando a gravação')
tq = tqdm(total=len(trades))
with open(os.path.join('dataset','trades_ltc_btc.csv'),'a') as c:
    anterior = float(config['ltc']['anterior'])
    for t in trades:
        atual = float(t['rate_close'])
        c.writelines(f"{t['time_period_end']};{t['rate_close']};{1 if atual > anterior else 0};{1 if atual <= anterior else 0}\n")
        anterior = atual
        datafim = t['time_period_end']
        tq.update(1)
    
config['ltc']['start'] = datafim
config['ltc']['anterior'] = str(anterior)
with open('config.ini','w') as file:
    config.write(file)
    