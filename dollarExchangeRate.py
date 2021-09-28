'Program to import a dollar exchange rate by API at the date provided by the user'

import requests
import pprint
year = input('Please enter the year within the range of 2002-2021: ' )
month = input('Please enter the month within the range of 01-12: ' )
day = input('Please enter the day within the range of 01-31: ' )
date = year + '-' + month + '-' + day

r = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/c/usd/{date}/?format=json')
# pprint.pprint(r.json())

json_dict = r.json()
print('currency: ', json_dict['code'])
print('date: ', json_dict['rates'][0]['effectiveDate'])
print('exchange rate: ', json_dict['rates'][0]['bid'])