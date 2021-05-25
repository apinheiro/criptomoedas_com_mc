from Helper.HMM import HistoricoTrades
import numpy as np

a = HistoricoTrades([1,2,3,4,5,4,2,3,45,6,4,2,2,1,3,4,6,7,4,2,4,3,5,6,7],profundidade = 5)

a.train([1,2,3,4,5,4,2,3,45,6,4,2,1,1,3,4,6,7,4,2,4,3,5,6,7])

print(a._cabecalho[np.argmax(a.matriz['DDESS'])])

#print(index)
#print(value)