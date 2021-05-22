import requests, json

# Método para retornar os símbolos.
# Com este método eu retornarei apenas os símbolos necessários para fazer a movimentação dos trades.
# Os símbolos utilizados foram
url = 'https://rest.coinapi.io/v1/symbols'
headers = {'X-CoinAPI-Key' : '14C54900-249E-4D61-BD8F-53B540EF49C9'}
response = requests.get(url, headers=headers)

saida = json.loads(response.text)

itens = [i for i in saida if i['exchange_id'] == 'BINANCE']

with open('simbolos.txt','w') as f:
    f.writelines(json.dumps(itens))