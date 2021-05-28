import configparser, sys, os
from datetime import datetime
from Helper.Dataset import Dataset, Criptos

codigo = sys.argv[1] if len(sys.argv) > 0 else 'btc'
print(codigo)
config = configparser.ConfigParser()
config.read('config.ini')

cfg = config[codigo]

try: 
   start = datetime.fromisoformat(cfg['start'][:-2])
except:
    start = None

print('Iniciando Consulta')
consulta = Criptos(cod_de = cfg['codigo_de'],cod_para = cfg['codigo_para'],data_inicio = start,data_limite= None)
print('Convertendo Json')

dataset = Dataset(consulta.obterTrades())
print('Iniciando a gravação')
config[codigo]['start'] = dataset.gerarArquivo(os.path.join('dataset',cfg['arquivo']))

with open('config.ini','w') as file:
    config.write(file)