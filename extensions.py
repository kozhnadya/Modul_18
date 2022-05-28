# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:24:12 2022

@author: zbookuser
"""

import requests
import json
from config import keys


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
                        
        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{quote}"')
            
        try:
            base_tiker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{base}"')
            
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}"')
        
        
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[base_tiker]
        
        return total_base