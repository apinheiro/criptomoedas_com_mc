import numpy as np
import pandas as pd

class HistoricoTrades(object):
    def __init__(self, dataset, profundidade= 1):
        self.dataset = dataset
        self.profundidade = profundidade
        self.retorno = []
        self.matriz = []
        self._cabecalho = []
        
    def train(self, X):
        self.dataset = X
        self.generate()
        self.matrizTransicao()
    '''
    ' Gerador de matriz de treinamento
    '
    ' A partir deste código, será possível gerar uma matriz com todos os possíveis estados e todas as possíveis transições de estados
    ' baseado no modelo a ser treinado.
    '
    ' Entrada: 
    '    dataset: conjunto com os valores dos trades, ordenados pela data em que o trade aconteceu. 
    '''
    def generate(self):
        anterior = 0.0
        memoria = self.profundidade * ['E']
        for item in self.dataset:
           operacao = 'S' if item > anterior else ('D' if item < anterior else 'E')
           self.retorno.append(''.join(memoria))
           memoria = memoria[1:] + [operacao]
           anterior = item

    def matrizTransicao(self):
        n = list(set(self.retorno)) #number of states
        self._cabecalho = n
        self.matriz = {}
        for i in n:
            self.matriz[i] = [0]*len(n)
            
        for (i,j) in zip(self.retorno,self.retorno[1:]):
            self.matriz[i][n.index(j)] += 1
        #now convert to probabilities:
        for row in self.matriz:
            s = sum(self.matriz[row])
            if s > 0:
                self.matriz[row] = [f/s for f in self.matriz[row]]