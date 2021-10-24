import pandas as pd
from collections import Counter
df = pd.read_csv('netflix_titles.csv')

dateTypeName = Counter(df['type']) 


print(dateTypeName)