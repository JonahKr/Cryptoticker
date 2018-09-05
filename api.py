import requests
import json
with open('config.json', 'r') as f:
    config = json.load(f)

# access config
ccapi_url = config['ccapi_url']
ccapi_listing_url = config['ccapi_listing_url']

# Check if the symbol really exists
def getCryptoProve(ccurrencylist):
	try:
		return_cryptourrencylist = []
		apidata = requests.get(ccapi_listing_url)
		data = json.loads(apidata.text)
		cryptocurrencylist = data["data"]
		#go through all cryptocurrencies and look if any of these is similar to one of the passed list
		for cryptocurrency in cryptocurrencylist:
			for currency in ccurrencylist:
				#does the passed symbol equal the cryptocurrency symbol?
				if(currency.upper()==cryptocurrency['symbol']):
					return_cryptourrencylist.insert(len(return_cryptourrencylist),currency.upper())
					print('Existance has been proved.')
					break
			#If the ammount of the passed list is reached, he don't has to test any further
			if(len(ccurrencylist)==len(return_cryptourrencylist)):
				break
		return return_cryptourrencylist
	except Exception as e:
		print str(e)
		return None
#
def getCryptoId(ccurrencylist):
	try:
		return_idlist = []
		apidata = requests.get(ccapi_listing_url)
		data = json.loads(apidata.text)
        #api cryptocurrencylist
		cryptocurrencylist = data["data"]
		#go through all cryptocurrencies and look if any of these is similar to one of the passed list
		for cryptocurrency in cryptocurrencylist:
			for currency in ccurrencylist:
				#does the passed symbol equal the cryptocurrency symbol?
				if(currency.upper()==cryptocurrency['symbol']):
					return_idlist.insert(len(return_idlist),cryptocurrency["id"])
					print('ID has been found.')
					break
			#If the ammount of the passed list is reached, he don't has to test any further
			if(len(ccurrencylist)==len(return_idlist)):
				break
		return return_idlist
	except Exception as e:
		print str(e)
		return None

def getCurrencyPriceById(ccidlist,fclist):
    try:
        print "trying priceget"
        print str(ccidlist)
        print str(fclist)
        ret_data = {}
        for id in ccidlist:
            for fc in fclist:
                print fc
                print id
                ret_data_sub={}
                print "before printtry"
                print (ccapi_url+"/"+str(id)+"/?convert="+fc)
                print "afterprinttry - before request"
                apidata = requests.get(ccapi_url+"/"+str(id)+"/"+"?convert="+fc)
                data = json.loads(apidata.text)
                print "aftertextload"
                price = round(float(data["data"]["quotes"][fc]["price"]), 2)
                ret_data_sub[fc]=price
            ret_data[id]=ret_data_sub
        return ret_data
    except Exception as e:
        print str(e)
        return None
