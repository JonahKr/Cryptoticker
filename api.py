import requests
import json
with open('api.json', 'r') as f:
    config = json.load(f)

# access config
ccapi_url = config['ccapi_url']
ccapi_listing_url = config['ccapi_listing_url']
supported_fiatcurrencies = config['supported_fiatcurrencies']

# Check if the symbol really exists


def getCryptoProve(ccurrencylist):
    try:
        return_cryptourrencylist = []
        apidata = requests.get(ccapi_listing_url)
        data = json.loads(apidata.text)
        cryptocurrencylist = data["data"]
        # go through all cryptocurrencies and look if any of these is similar to one of the passed list
    # cryptocurrency: all cryptocurrencies which are in the api
    # ccurrency :     all cryptocurrencies
        for cryptocurrency in cryptocurrencylist:
            for ccurrency in ccurrencylist:
                # does the passed symbol equal the cryptocurrency symbol?
                if(ccurrency.upper() == cryptocurrency['symbol']):
                    return_cryptourrencylist.append(ccurrency.upper())
                    print(
                        cryptocurrency['name'] + " \t(" + cryptocurrency['symbol'] + ") \t has been proved to exist.")
                    break
            # If the ammount of the passed list is reached, he don't has to test any further
            if(len(ccurrencylist) == len(return_cryptourrencylist)):
                break
    # END of the loop
        return return_cryptourrencylist

    except Exception as e:
        print(str(e))
        return None

# Check if the symbol really exists


def getFiatProve(fcurrencylist):
    try:
        ret_fcurrencylist = []
        for fcurrency in fcurrencylist:
            for supported_fiatcurrency in supported_fiatcurrencies:
                if(supported_fiatcurrency == fcurrency.upper()):
                    ret_fcurrencylist.append(supported_fiatcurrency)
                    print("\t\t(" + fcurrency + ")\t has been proved to exist.")
                    break
            if(ret_fcurrencylist[len(ret_fcurrencylist) - 1] != fcurrency.upper()):
                print("\n!!! Couldn't find \"" + fcurrency +
                      "\" as a valid currency. Please recheck. !!!\n")

        # after for loops
        return ret_fcurrencylist
    except Exception as e:
        print(str(e))
        return None

# Returns a list with all crypto ids for direkt api request


def getCryptoId(ccurrencylist):
    try:
        return_idlist = []
        apidata = requests.get(ccapi_listing_url)
        data = json.loads(apidata.text)
    # api cryptocurrencylist
        cryptocurrencylist = data["data"]
        # go through all cryptocurrencies and look if any of these is similar to one of the passed list
        for cryptocurrency in cryptocurrencylist:
            for currency in ccurrencylist:
                # does the passed symbol equal the cryptocurrency symbol?
                if(currency.upper() == cryptocurrency['symbol']):
                    return_idlist.append(cryptocurrency["id"])
                    break
            # If the ammount of the passed list is reached, he don't has to test any further
            if(len(ccurrencylist) == len(return_idlist)):
                break
        return return_idlist
    except Exception as e:
        print(str(e))
        return None

# returns data like data_example_data.json


def getCurrencyPriceById(ccidlist, fclist):
    try:
        ret_data = {}
        for id in ccidlist:
            ret_data_sub = {}
            for fc in fclist:
                apidata = requests.get(
                    ccapi_url + "/" + str(id) + "/" + "?convert=" + fc)
                data = json.loads(apidata.text)
                price = round(float(data["data"]["quotes"][fc]["price"]), 2)
                ret_data_sub[fc] = price
            ret_data[id] = ret_data_sub
        return ret_data
    except Exception as e:
        print(str(e))
        return None

# returns data like data_example_change.json of 24h change


def get24hChange(ccidlist):
    try:
        ret_data = {}
        for id in ccidlist:
            apidata = requests.get(ccapi_url + "/" + str(id) + "/")
            data = json.loads(apidata.text)
            change = data["data"]["quotes"]["USD"]["percent_change_24h"]
            ret_data[id] = change
        return ret_data
    except Exception as e:
        print(str(e))
        return None

# returns data like data_example_change.json of 7d change


def get7dChange(ccidlist):
    try:
        ret_data = {}
        for id in ccidlist:
            apidata = requests.get(ccapi_url + "/" + str(id) + "/")
            data = json.loads(apidata.text)
            change = data["data"]["quotes"]["USD"]["percent_change_7d"]
            ret_data[id] = change
        return ret_data
    except Exception as e:
        print(str(e))
        return None

# returns data like data_example_change.json of 1h change


def get1hChange(ccidlist):
    try:
        ret_data = {}
        for id in ccidlist:
            apidata = requests.get(ccapi_url + "/" + str(id) + "/")
            data = json.loads(apidata.text)
            change = data["data"]["quotes"]["USD"]["percent_change_1h"]
            ret_data[id] = change
        return ret_data
    except Exception as e:
        print(str(e))
        return None
