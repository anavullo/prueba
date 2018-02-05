# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import pandas as pd
specie = pd.read_csv ('http://gdfa.ugr.es/docencia/ecoinformatica/mano_de_muerto.csv')
specie.describe()
print(specie)
specie['continent'].value_counts()


#Tutorial de pandas de 10 min

import numpy as np
import matplotlib.pyplot as plt

s= pd.Series ([1,3,5,np.nan,6,8])
print (s)


dates = pd.date_range('20130101',periods=6)
dates

df = pd.DataFrame(np.random.randn(6,4), index=dates,columns=list('ABCD'))
df


df= df.cumsum()

fig = df.plot()
fig=plt.gcf()
fig.savefig('graficodf.pdf')
