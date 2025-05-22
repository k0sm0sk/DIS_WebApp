import pandas as pd

raw_data = pd.read_csv('data_raw.csv')
raw_data.groupby('title')

