'''Program allows to get an information about flats prices and location from one of the most famous site with auctions in Poland.
These information are redirected to the database'''

from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv

def parse_price(price):
    return float(price.replace(' ', '').replace('zł', '').replace(',','.'))

def parse_page(number):
    print(f'I am working on the page {number}')
    page = get(f'{URL}&page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    for offer in bs.find_all('div', class_='offer-wrapper'):
        footer = offer.find('td', class_='bottom-cell')
        location = footer.find('small', class_='breadcrumb').get_text().strip().split(',')[0]
        title = offer.find('strong').get_text().strip()
        price = parse_price(offer.find('p', class_='price').get_text().strip())

        cursor.execute("INSERT INTO offers VALUES (?, ?, ?)", (title, price, location))

    db.commit()

URL = 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/mazowieckie/?search%5Bfilter_enum_rooms%5D%5B0%5D=one'
db = sqlite3.connect('flat.db')
cursor = db.cursor()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute("CREATE TABLE offers (name TEXT, price REAL, city TEXT)")
    quit()

l = int(input('Please to input pieces of pages: '))
for page in range(1,l):
    parse_page(page)

db.close()