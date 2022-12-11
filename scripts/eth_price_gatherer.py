import pandas as pd
import json
import requests
import datetime
import time

start_date = datetime.datetime.now()
target_date = datetime.datetime(2021, 10, 1)

BASE = "https://api.polygon.io/v2/aggs/ticker/X:ETHUSD/range/{}/{}/{}/{}?adjusted=true&sort=asc&limit=50000&apiKey=2CiMnHo26Rsl7EfHzQHNnASWAHcKUvLB"
PATH = "../ETH_DATA/nfp_eth_{}_{}_price.csv"

cpi_dates = [[2022, 10, 13], [2022, 9, 13], [2022, 8, 10], [2022, 7, 13], [2022, 6, 10], [2022, 5, 11], [2022, 4, 12], [2022, 3, 10]]
fomc_dates = [[2022, 11, 2], [2022, 9, 21], [2022, 7, 27], [2022, 6, 15], [2022, 5, 4], [2022, 3, 16], [2022, 1, 26]]
nfp_dates = [[2022, 12, 2], [2022, 11, 4], [2022, 10, 7], [2022, 9, 2], [2022, 8, 5], [2022, 7, 8], [2022, 6, 3], [2022, 5, 6], [2022, 4, 1], [2022, 3, 4], [2022, 2, 4]]

df = pd.DataFrame(columns=['v', 'vw', 'o', 'c', 'h', 'l', 't', 'n'])
for dates_list in [nfp_dates]:
    for date in dates_list:
        start_date = datetime.datetime(date[0], date[1], date[2])
        end_date = start_date - datetime.timedelta(days=2)
        print(end_date.strftime("%Y-%m-%d"))
        print(BASE.format(5, "minute", end_date.strftime("%Y-%m-%d"), start_date.strftime("%Y-%m-%d")))
        resp = requests.get(BASE.format(5, "minute", end_date.strftime("%Y-%m-%d"), start_date.strftime("%Y-%m-%d")))
        my_dic = resp.json()
        print(my_dic.keys())
        print(type(my_dic))
        my_df = pd.DataFrame(my_dic["results"])
        print(my_df)
        df = pd.concat([my_df, df]).reset_index(drop=True)
        time.sleep(15)

print(df)

path = PATH.format(5, "minute")
try:
    open(path, 'x')
except:
    pass
file = open(path, 'w')
df.rename(
    columns=({ 'v': 'volume', 
               'vw': 'volume_weighted_average_price',
               'o': 'open',
               'c': 'close',
               'h': 'high',
               'l': 'low',
               't': 'time',
               'n': 'number_transactions'}), 
    inplace=True,
)
df.to_csv(file, index=False)