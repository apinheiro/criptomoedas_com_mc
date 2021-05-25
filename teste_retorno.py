from Helper.HMM import HistoricoTrades

a = HistoricoTrades([1,2,3,4,5,4,2,3,45,6,4,2,1,3,4,6,7,4,2,4,3,5,6,7],profundidade = 3)

a.train([1,2,3,4,5,4,2,3,45,6,4,2,1,3,4,6,7,4,2,4,3,5,6,7])

k = a.df.loc[a.df.origem == '001']
k['001'] += 1
print(k)
#print(index)
#print(value)