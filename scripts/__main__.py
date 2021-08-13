# imports

import requests
import time
import key


# class

class currency:
    def __init__(self, datapoints, coinid):
        self.datapoints = datapoints
        self.coinid = coinid

    @classmethod
    def new_instance(a, b):
        return currency('', 0)


mycoin1 = currency('', 0)
coins = []

# variables

headers = {
    'X-CMC_PRO_API_KEY': key.apikey,
    'Accepts': 'application/json'
}

payload = {
    'start': '1',
    'limit': '',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# functions


def crypto_list():
    '''Lists available cryptocurrencies.'''

    print("Available cryptocurrencies and their id numbers: BTC = 1")
    print("ETH = 1027, BNB = 1839, XRP = 52, USDT = 825, DOGE = 74")
    print("ADA = 2010, DOT = 6636, LTC = 2, BCH = 1831, UNI = 7083")
    print("LINK = 1975, VET = 3077, XLM = 512, THETA = 2416")
    print("USDC = 3408, FIL = 2280, TRX = 1958, WBTC = 3717")
    print("SOL = 5426, EOS = 1765, NEO = 1376, KLAY = 4256")
    print("BSV = 3602, XMR = 328, MIOTA = 1720, BUSD = 4687, BTT = 3718")
    print("CRO = 3635, LUNA = 4172, AAVE = 7278, XTZ = 2011, FTT = 4195")
    print("ATOM = 3794, ALGO = 4030")


def set_payload_limit():
    '''Gives the user the chance to set the payload limit for the API call.'''

    question = str(input("Do you want to set a payload limit? If not, the limit will automatically be set to 5000. 'y' or 'n': "))
    if question == 'y':
        limit = str(input("Set your payload limit: "))
        return limit
    elif question == 'n':
        limit = '5000'
        return limit


def transfer_payload():
    '''Transfers chosen payload limit to its dictionary value.'''

    payload['limit'] = set_payload_limit()


def which_id():
    '''Returns the id number of the currency in the Coinmarketcap API'''

    idnum = int(input("Enter the id number of the currency: "))
    return idnum


def new_coin():
    '''Pulls data of chosen coins, crates class instances and puts the pulled
    data for each coin into a corresponding instance.'''

    while True:
        answer = str(input("Do you want to add a new coin, 'y' or 'n'? "))

        if answer == 'y':
            idtoclass() # gets the coin ID and puts it into mycoin1.coinid
            points_to_class() # gets the coin data and puts it into mycoin1.datapoints
            coins.append(currency.new_instance(1)) # make new class instance new_instance(1) and puts that class instance in a list
            coins[-1].datapoints = mycoin1.datapoints # gives mycoin1 datapoints to last instance
            coins[-1].coinid = mycoin1.coinid # gives mycoin1 coinid to last instance
        elif answer == 'n':
            break


def idtoclass():
    '''Transfers the coin id to a class instance variable'''

    mycoin1.coinid = which_id()


def get_coin_data(x):
    '''Iterates through the list of coins with the payload parameters
    and searches for the one with the correct id number given by the x
    parameter(which_id() function). Returns datapoints'''

    points = []
    json = requests.get(url, params=payload, headers=headers).json()
    coins = json['data']

    for coin in coins:
        if coin['id'] == x:
            point0 = coin['symbol']
            points.append(point0)

    for coin in coins:
        if coin['id'] == x:
            point1 = round(coin['quote']['USD']['price'], 5)
            points.append(point1)

    for coin in coins:
        if coin['id'] == x:
            point2 = round(coin['quote']['USD']['percent_change_1h'], 5)
            points.append(point2)

    for coin in coins:
        if coin['id'] == x:
            point3 = round(coin['quote']['USD']['percent_change_24h'], 5)
            points.append(point3)

    for coin in coins:
        if coin['id'] == x:
            point4 = round(coin['quote']['USD']['percent_change_7d'], 5)
            points.append(point4)

    for coin in coins:
        if coin['id'] == x:
            point5 = coin['quote']['USD']['last_updated']
            points.append(point5)

    return points


def points_to_class():
    '''Transfers coin data from get_coin_data() into a class instance variable.'''
    mycoin1.datapoints = get_coin_data(mycoin1.coinid)


def call_data(myco):
    '''Calls the data and prints it.'''

    transfer_payload()
    crypto_list()
    new_coin()
    print("Coin", "\t", "price", "\t", "\t", "Change 1h", "\t", "Change 24h", "\t", "Change 7d", "\t", "Last updated")

    while True:
        for coin in myco:
            print(coin.datapoints[0], '\t', coin.datapoints[1], '\t', coin.datapoints[2], '\t', coin.datapoints[3], '\t', coin.datapoints[4], '\t', coin.datapoints[5])
            coin.datapoints.clear()
            coin.datapoints = get_coin_data(coin.coinid)
        time.sleep(60)
        print('\n')


if __name__ == "__main__":
    call_data(coins)
