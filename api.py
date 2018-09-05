import requests
import argparse
import json
with open('config.json', 'r') as f:
    config = json.load(f)

# access config
ccapi_url = config['ccapi_url']


parser = argparse.ArgumentParser(description='Crypto Ticker')
parser.add_argument('-cc', '--cryptocurrency', dest='cryptocurrency',
                    help='The symbol of the currency you want to be displayed.(standard: BTC)', type=String)
args = parser.parse_args()


def getCurrencyPrice(cc):
    # https://api.coinmarketcap.com/v1/ticker
	try:
		symbol = c.upper()
		apidata = requests.get('ccapi_url')
		data = json.loads(apidata.text)
		for currency in data:
			if (currency['symbol'] == symbol):
				price = "{0:.2f}".format(round(float(currency['price_usd']), 2))
				return price
		print ("Couldn't find data")
		return None
	except Exception as e:
		print str(e, 'utf-8')
		return None

def getCurrency24hRate(cc):
	try:
		symbol = c.upper()
		apidata = requests.get('ccapi_url')
		data = json.loads(apidata.text)
		for currency in data:
			if (currency['symbol'] == symbol):
				price = "{0:.2f}".format(round(float(currency['price_usd']), 2))
				return price
		print ("Couldn't find data")
		return None
	except Exception as e:
		print str(e, 'utf-8')
		return None
