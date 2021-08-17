# class


class currency:
    def __init__(self, datapoints, coinid, ticker):
        self.datapoints = datapoints
        self.coinid = coinid
        self.ticker = ticker

    @classmethod
    def new_instance(a, b):
        '''Creates new instance of the class.
        Called by functions.new_coin()'''

        return currency('', 0, '')


mycoin1 = currency('', 0, '')
coins = []  # list for stashing the chosen currencies for later iteration
