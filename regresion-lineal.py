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

#Se grafica las cantidades de movies por año
plt.bar(dataCount.keys(),dataCount.values())
plt.xlabel('YEARS')
plt.ylabel('COUNT')
plt.title("MOVIE BY YEAR")
plt.show()
print(dataCount)