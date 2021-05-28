from Helper.MC import CadeiaMarkov
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

csv = pd.read_csv('dataset/trades_btc_usd.csv', header=0, sep=';')
print(csv.head())

x_train, x_test, y_train, y_test = train_test_split(csv['fechamento'], csv['ganho'], random_state = 42, test_size=0.1)
print(len(x_test), len(y_test))

a = CadeiaMarkov(profundidade = 5)
a.train(x_train)

print(a._cabecalho)

print(a.predict('SDD'))
print("Score : {}".format(a.score(x_test, y_test)))
#print(index)
#print(value)