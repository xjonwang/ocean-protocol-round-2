import pandas as pd
import numpy as np

cpi_data = pd.read_csv("../ETH_DATA/cpi_eth_5_minute_price.csv")
spot_price = input("Input the spot price: ")
#print(cpi_data)
my_dic = pd.DataFrame(columns=['t+12', 't+24', 't+25', 't+26', 't+27', 't+28', 't+29', 't+30', 't+31', 't+32', 't+33', 't+34', 't+35', 't+36', 't+48', 't+54'])

for i in range(0, len(cpi_data), 864):
    day = cpi_data.loc[i : i + 863]
    #print(day)
    t0 = day.loc[i + 12 * 24]['close']
    temp = pd.DataFrame(columns=['t+12', 't+24', 't+25', 't+26', 't+27', 't+28', 't+29', 't+30', 't+31', 't+32', 't+33', 't+34', 't+35', 't+36', 't+48', 't+54'], index=[0])
    times = [12, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 48, 54]
    for j in range(0, 16):
        temp.loc[0][j] = day.loc[i + 12 * times[j]]['close'] / t0;
    my_dic = pd.concat([my_dic, temp])

#print(my_dic)
my_dic = my_dic.mul(int(spot_price))
print(my_dic.mean())
print()
print(my_dic.median())
print()
print(my_dic.std())
