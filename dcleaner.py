import pandas as pd

raw_data = pd.read_csv('data_raw.csv')
sorted_data = raw_data.sort_values('title')

sorted_data.to_csv('data_sorted.csv', index=False)


last_title = None
cleaned_df = pd.DataFrame()
for row in range(len(sorted_data)):
    title_name = sorted_data.loc[row, 'title']
    sales = sorted_data.loc[row, 'total_sales']
    if title_name == last_title:
        

    
    if sales:
        
    last_title = title_name







