from genericpath import isfile
from tqdm import tqdm
import os, json

class Dataset(object):
    
    def __init__(self, json_file, sep=';'):
        self.extrairInformacoes(json_file)
        self.sep = sep
        
                
    def extrairInformacoes(self, json_file):
        self.trades = json_file
        
    def gerarArquivo(self,nome = str):
        tq = tqdm(total=len(self.trades))
        datafim = ''
        cabecalho = "data;abertura;fechamento;maxima;minima\n" if not isfile(nome) else None
        with open(nome,'a') as file:
            if not cabecalho is None:
                file.writelines(f"{cabecalho}")
            for t in self.trades:
                file.writelines(f"{t['time_period_end'][:-1]};{t['rate_open']};{t['rate_close']};{t['rate_high']};{t['rate_low']}\n")
                datafim = t['time_period_end']
                tq.update(1)
        return datafim
           

from datetime import datetime
import requests
from datetime import datetime

########################
########################

class Criptos(object):
    
    def __init__(self,cod_de = '', cod_para = '', num_trades = 50000, data_inicio = '', data_limite = datetime):
        self.cod_de = cod_de
        self.cod_para = cod_para
        self.trades = num_trades
        self.data_inicio = data_inicio if not data_inicio is None else datetime(2016,1,1,0,0,0)
        self.data_limite = data_limite if not data_limite is None else datetime.now()
        self.period = '1HRS'
        
        self.__url = 'https://rest.coinapi.io/v1/exchangerate/{}/{}/history'.format(self.cod_de, self.cod_para)
        self.__chaves = ['14C54900-249E-4D61-BD8F-53B540EF49C9',
                         '70AA6AE1-90B0-481E-B9CF-998A3F592705']
        
    def obterTrades(self, qtde = None):
        qtde = self.trades if qtde is None else qtde
        
        return self.__trades(qtde)
    
    def __trades(self,qtde):
        for chave in self.__chaves:
            headers = {'X-CoinAPI-Key' : chave}
            format = "%Y-%m-%dT%H:%M:%S"
            url = f"{self.__url}?limit={qtde}&period_id={self.period}&time_start={self.data_inicio.strftime(format)}&time_end={self.data_limite.strftime(format)}"
            response = requests.get(url, headers=headers)
            js = json.loads(response.text)
            if 'error' in js:
                continue
            return js
        
        raise Exception('As chaves informadas já foram usadas. Favor aguardar mais 24 horas até usá-las novamente.')