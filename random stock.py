import random
import pandas as pd

payload = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
sp500 = payload[0]
random_row = sp500.sample(1)
random_stock = random_row['Security'].values[0]
random_symbol = random_row['Symbol'].values[0]
print("Randomly selected stock from S&P 500:", random_symbol, "-", random_stock)