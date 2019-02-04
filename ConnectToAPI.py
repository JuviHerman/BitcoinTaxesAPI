import pandas as pd
import requests

application = "XXXXXX" #name of project
headers  = {"Content-Type": "application/json","UserAgent": application }

Year = '2017'
params = {"taxyear" : Year,"start" : '0', "limit": '1000'}

apikey = 'abcd'
apisecret = 'kjshdgfkihsgdf'
Authorization = (apikey, apisecret)

resp = requests.get('https://api.bitcoin.tax/v1/transactions/',headers = headers,params=params, auth = Authorization )

print(resp)
if resp.status_code != 200:
    # This means something went wrong.
    pass
res = resp.json()
for x,i in enumerate(res['data']['transactions']):
    print(i)
    print(x+1)



