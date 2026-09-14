import pandas as pd
import numpy as np


data = pd.read_csv('data.csv', encoding='latin1')

print(data.shape)
print(data.head())
print(data.info())

print(data.isnull().sum())