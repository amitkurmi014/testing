import requests
from parsel import Selector


for i in range(1,2):
    r = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')
    response = Selector(text=r.text)


def tittle(response):
    # for list in response.xpath('//li/article'):
        title = response.xpath('.//h3/a/text()').get()
        return(title)
        

def product_price(response):
    # for list in response.xpath('//li/article'):
        price = response.xpath('.//p[@class="price_color"]/text()').get()
        return(price)


def available(response):
    # for list in response.xpath('//li/article'):
        s_available = response.xpath('.//p[@class="instock availability"]/text()').get().split()[1]
        return s_available


def url(response):
    # for list in response.xpath('//li/article'):
        image_url = response.xpath('.//img/@src').get()
        final_url = "https://books.toscrape.com/" + image_url 
        return final_url          


def rating(response):
    # for list in response.xpath('//li/article'):
        rate = response.xpath('.//p[@class]').get().split(' ')[2]
        return (rate)                

for content in response.xpath('//li/article'):
  print(f"""
tittle: {tittle(content)}
price: {product_price(content)}
available: {available(content)}
image_url: {url(content)}
rating: {rating(content)}
""")
