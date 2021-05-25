import numpy as np
import pandas as pd

class HistoricoTrades(object):
    def __init__(self, dataset, profundidade= 1):
        self.dataset = dataset
        self.profundidade = profundidade
        self.retorno = [[0],[self.profundidade*[0]]]

    def train(self, X):
        self.dataset = X
        self.generate()
        itens = np.unique(np.array(["".join(map(str,k)) for k in self.retorno[1]]))
        dataset = {i : len(itens)*[0] for i in itens}

        self.df = pd.DataFrame(dataset)
        self.df['origem'] = itens
        self.df.set_index('origem')
        self.populaDataset()

    def populaDataset(self):
        anterior = '000'
        for i in self.retorno[0]:
            atual = "".join(map(str,i))
            k = self.df.loc[self.df.origem == atual].index

    def generate(self):
        anterior = 0.0
        memoria = self.profundidade * [0]
        for item in self.dataset:
           operacao = 1 if item > anterior else 0
           self.retorno[0].append(operacao)
           self.retorno[1].append(memoria)
           memoria = memoria[1:] + [operacao]
           anterior = item
