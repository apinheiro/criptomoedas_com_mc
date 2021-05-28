import numpy as np
import pandas as pd

class CadeiaMarkov(object):
    def __init__(self, dataset = None, profundidade= 1):
        self.dataset = dataset
        self.profundidade = profundidade
        self.retorno = []
        self.matriz = []
        self._cabecalho = []
        
    def train(self, X):
        self.dataset = X
        self.generate()
        self.__matrizTransicao()
        self.__otimizarMatriz()
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
        self.retorno, y = self.__gerarMemoria(self.dataset)

    def __gerarMemoria(self, dataset, y_list = False):
        anterior = 0.0
        memoria = self.profundidade * ['E']
        retorno = []
        y = []
        for item in dataset:
           operacao = 'S' if item > anterior else ('D' if item < anterior else 'E')
           if y_list:
               y.append(operacao)
           retorno.append(''.join(memoria))
           memoria = memoria[1:] + [operacao]
           anterior = item
        return retorno, y

    def __matrizTransicao(self):
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
    
    def score(self, x_test, y_test):
        # 1 - Gera a sequência de trades a serem realizados.
        # 2 - Verifica a probabilidade de ser um trade de ganho, perda ou empate
        # 3 - Verifica se o próximo trade é o trade a ser gerado.
        x, y = self.__gerarMemoria(x_test, True)
        x = x[self.profundidade:]
        y = y[self.profundidade:]
        
        score = [1 for i in range(len(x)) if self.predict(x[i]) == y[i]]
        #score = 0
        #for i in range(len(x)):
        #    score += 1 if self.predict(x[i]) == y[i] else 0
            
        return sum(score)/len(y)
    
    def predict(self,x_value):
        index, m = self.__indexPredict(x_value=x_value)
        j = index % len(self._cabecalho)
       
        return self._cabecalho[j][-1:]
    
    def __indexPredict(self,x_value):
        if sum([1 for k in self._cabecalho if k.endswith(x_value)]) > 0:
           # TODO: Se o índice não for encontrado, encontrar os casos onde o índice termina
           # com o valor informado.
           keys = [k for k in self._cabecalho if k.endswith(x_value)]
           resultados = [self.matriz[i] for i in keys]
           x = np.matrix(resultados)
           index_array = x.argmax()
           return index_array, resultados
        else:
           return self.__indexPredict(x_value[1:])
    
    def scorePredict(self, x_value):
       index, m = self.__indexPredict(x_value=x_value)
       i = int(index/len(self._cabecalho))
       j = index % len(self._cabecalho)
       
       return m[i][j]
       