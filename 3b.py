
import pandas as pd
from numpy import unique
from pandas import read_csv

data = pd.read_csv('3oil-spill.csv', header=None)

print(data.nunique())

print(data.shape)

counts = data.nunique()

to_del = [i for i,v in enumerate(counts) if v == 1]
print(to_del)
data.drop(to_del, axis=1, inplace=True)
print(data.shape)
