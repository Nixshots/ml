from numpy import unique
from pandas import read_csv
import pandas as pd

# summarize the number of unique values for each column using numpy
# load the dataset
data = pd.read_csv('3iris.csv', header=None)
# calculate duplicates
dups = data.duplicated()
# report if there are any duplicates
print(dups.any())
# list all duplicate rows
print(data[dups])

# delete rows of duplicate data from the dataset

print(data.shape)
# delete duplicate rows
data.drop_duplicates(inplace=True)
print(data.shape)
