import requests
from parsel import Selector


for i in range(1,51):
    r = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')
    response = Selector(text=r.text)


def tittle(response):
    for list in response.xpath('//li/article'):
        title = list.xpath('.//h3/a/text()').get()
        print(title) 
        

def price(response):
    for list in response.xpath('//li/article'):
        price = list.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[1]').get()
        print(price)


def available(response):
    for list in response.xpath('//li/article'):
        available = list.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[2]').getall()
        print(available)


def url(response):
    for list in response.xpath('//li/article'):
        image_url = list.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/div[1]/a/img').get()
        
        print(image_url)           


def rating(response):
    for list in response.xpath('//li/article'):
        rating = list.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/p').getall()
        print(rating)                  


print(f"""
tittle: {tittle(response)}
price: {price(response)}
available: {available(response)}
image_url: {url(response)}
rating: {rating(response)}
""")
