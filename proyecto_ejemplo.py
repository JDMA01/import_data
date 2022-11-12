from urllib.request import urlretrieve
import pandas as pd

url= 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url,'winequality-white.csv')
df = pd.read_csv ('winequality-white.csv', sep=';')
print (df.head())