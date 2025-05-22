import pandas as pd
from tqdm import tqdm

raw_data = pd.read_csv('../data/raw.csv')

sorted_data = raw_data.sort_values('title')
sorted_data.to_csv('../data/sorted.csv', index=False)

game_sales = 0
biggest_sale = 0
largest_platform = None
box_cover = None
cleaned_df = pd.DataFrame()
for row in tqdm(range(len(sorted_data)-1)):
    current_df = sorted_data.iloc[row:row+1]
    next_df = sorted_data.iloc[row+1:row+2]

    if current_df.iloc[0]['title'] == next_df.iloc[0]['title']:
        if not pd.isna(current_df.iloc[0]['total_sales']):
            game_sales += current_df.iloc[0]['total_sales']
            if current_df.iloc[0]['total_sales'] > biggest_sale:
                biggest_sale = current_df.iloc[0]['total_sales']
                largest_platform = current_df.iloc[0]['console']
                box_cover = current_df.iloc[0]['img']
    else:
        if (game_sales == 0 or pd.isna(game_sales)) and pd.isna(current_df.iloc[0]['total_sales']):
            continue
        else:
            # print(f"Added {current_df.iloc[0]['title']}, because:")
            # print(f"game_sales = {game_sales}")
            # print(f"total_sales = {current_df.iloc[0]['total_sales']}")
            if not pd.isna(current_df.iloc[0]['total_sales']):
                if current_df.iloc[0]['total_sales'] > biggest_sale:
                    biggest_sale = current_df.iloc[0]['total_sales']
                    largest_platform = current_df.iloc[0]['console']
                    box_cover = current_df.iloc[0]['img']
                game_sales += current_df.iloc[0]['total_sales']
            current_df.at[current_df.index[0], 'total_sales'] = game_sales
            current_df.at[current_df.index[0], 'console'] = largest_platform
            current_df.at[current_df.index[0], 'img'] = box_cover
            cleaned_df = pd.concat([cleaned_df, current_df])
            biggest_sale = 0
            game_sales = 0

cleaned_df.to_csv('../data/cleaned.csv', index=False)





