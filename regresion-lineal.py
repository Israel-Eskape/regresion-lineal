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

movie = df.loc[df.loc[:,'type'] == 'Movie']
movieYear = movie.loc[:,['type','release_year']]

dataCount = Counter(movieYear['release_year'])


print(dataCount)