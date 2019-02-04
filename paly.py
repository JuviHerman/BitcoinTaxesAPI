import pandas as pd
import requests
headers  = {"Content-Type": "application/json","UserAgent": "RonG poloniex"}
params = {"taxyear" : '2017',"start" : '0', "limit": '1000'}
Authorization = ('2d1242924df291ca', '06486dd0306a07b0409468e6af1fdc77')
resp = requests.get('https://api.bitcoin.tax/v1/transactions/',headers = headers,params=params, auth = Authorization )
print(resp)
if resp.status_code != 200:
    # This means something went wrong.
    pass
res = resp.json()
for x,i in enumerate(res['data']['transactions']):
    print(i)
    print(x+1)



