import requests, json
from tqdm import tqdm
from datetime import datetime

start = datetime(2021,1,1,0,0,0)
end = datetime.now()
url = 'https://rest.coinapi.io/v1/exchangerate/LTC/BTC/history?limit=50000&period_id=1HRS&time_start={}&time_end={}'.format(start.strftime("%Y-%m-%dT%H:%M:%S"),end.strftime("%Y-%m-%dT%H:%M:%S"))

headers = {'X-CoinAPI-Key' : '14C54900-249E-4D61-BD8F-53B540EF49C9'}
print('Iniciando Consulta')
response = requests.get(url, headers=headers)
print(response.text)
print('Convertendo Json')
trades = json.loads(response.text)

print('Iniciando a gravação')
tq = tqdm(total=len(trades))
with open(os.path.join('dataset','trades_btc_usd.csv'),'w') as c:
    c.writelines('hora;fechamento;ganho;perda')
    anterior = 0.0
    for t in trades:
        atual = float(t['rate_close'])
        c.writelines(f"{t['time_period_en']};{t['rate_close']};{1 if atual > anterior else 0};{1 if atual <= anterior else 0}")
        tq.update(1)
    
