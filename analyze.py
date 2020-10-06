import pandas as pd
from urllib.parse import urlparse

hostnames = {}
df = pd.read_csv('scrapy_game_input.csv')
for i, row in df.iterrows():
    h = urlparse(row['url']).netloc
    hostnames[h] = hostnames.get(h, 0) + 1

print(hostnames)
# hostnames = list(hostnames)
# print(len(hostnames))
# print('\n'.join(hostnames))
# hostnames = urlparse()