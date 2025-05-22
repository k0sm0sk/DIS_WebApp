import pandas as pd

raw_data = pd.read_csv('data_raw.csv')
sorted_data = raw_data.sort_values('title')

sorted_data.to_csv('data_sorted.csv', index=False)

print(sorted_data)






