import requests
from parsel import Selector


for i in range(1,51):
    r = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')
    response = Selector(text=r.text)
    
    