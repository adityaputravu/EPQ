import requests

FILENAME = 'data.json'

token = 'UK5443TGX2HXZX96'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=SPY&apikey={token}'
req = requests.get(url)
data = req.text

for i in range(1,8):
	data = data.replace(f'{i}. ', '')

if req.status_code == 200:
	with open(FILENAME, 'w') as f:
		f.write(data)
