from numpy import unique
from pandas import read_csv
import pandas as pd


data = pd.read_csv('3iris.csv', header=None)

dups = data.duplicated()

print(dups.any())

print(data[dups])



print(data.shape)

data.drop_duplicates(inplace=True)
print(data.shape)
