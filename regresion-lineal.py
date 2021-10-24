import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

from pandas.core.frame import DataFrame
df = pd.read_csv('netflix_titles.csv')

#dataTypeName = Counter(df['type']) #.keys() and .value()
#dataTypeRelease = Counter(df['release_year'])


#movie = df.loc[:,'type'] == 'Movie'
#moviedf = df.loc[movie]

movie = df.loc[df.loc[:,'type'] == 'Movie'] # Marca con true los valores de la columna type que sean movie y después 
                                            #obtiene todas las filas que están marcadas con true
movieYear = movie.loc[:,['type','release_year']] #Obtengo solo las dos columnas type & release_year
dataCount = Counter(movieYear['release_year']) #Cuenta cuantas veces se repiten cada valor en la columna release_year


tvShow = df.loc[df.loc[:,'type'] == 'TV Show']
tvShowYear = tvShow.loc[:,['type','release_year']]
tvdataCounter = Counter(tvShowYear['release_year'])

print(dataCount)
print(tvdataCounter)

#Se grafica las cantidades de movies por año
plt.bar(dataCount.keys(),dataCount.values(),label = 'Movie',color = 'g')
plt.bar(tvdataCounter.keys(),tvdataCounter.values(), label = 'Tv Show')
plt.xlabel('YEARS')
plt.ylabel('COUNT')
plt.title("MOVIE BY YEAR")
plt.legend()
plt.show()
print(dataCount)
