from collections import OrderedDict

import rumps
from json import loads
import requests

class EthereumTicker(rumps.App):
    ICON = "./static/eth.ico"
    UPDATE_FREQUENCY = 60
    
    #TODO: Use endpoint that offers more currencies
    DEFAULT_CURRENCY = "USD"
    ETH_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum"
    SYMBOLS = OrderedDict([
        ("USD" , "$")
    ])

    def __init__(self):
        super(EthereumTicker, self).__init__(type(self).__name__, icon=EthereumTicker.ICON)
        self.padded = False
        self.currency = EthereumTicker.DEFAULT_CURRENCY
        self.run()
    
    @rumps.timer(UPDATE_FREQUENCY)
    def update_price(self, sender):
        res = requests.get(EthereumTicker.ETH_URL)
        curr_price = loads(res.text)[0]['current_price']
        title = "$" + str(curr_price)
        self.title = title

if __name__ == '__main__':
    EthereumTicker()