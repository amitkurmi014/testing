import requests
from parsel import Selector
import json
 
data =[]

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
        s_available = response.xpath('.//p[@class = "instock availability"]/text()').getall()
        clean =''.join(x.strip() for x in  s_available if x.strip())
        return clean
        # another way
        # if s_available:
        #     s_available = s_available.split()[1]
        # else:
        #     "Out of stock"
        


def url(response):
    # for list in response.xpath('//li/article'):
        image_url = response.xpath('.//img/@src').get()
        final_url = "https://books.toscrape.com/" + image_url 
        return (final_url)          


def rating(response):
    # for list in response.xpath('//li/article'):
        rate = response.xpath('.//p/@class').get().split()[1]
        return (rate)                

for i in range(1,51):
    r = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')
    response = Selector(r.text)
    for content in response.xpath('//li/article'):
        web_data = {
            "tittle": tittle(content),
            "price": product_price(content),
            "availability": available(content),
            "image_url": url(content),
            "rating": rating(content)
        }
        data.append(web_data)
    
    with open("data.json","w",encoding='utf-8') as d:
        json.dump(data,d,ensure_ascii=False,indent=4)
    
    print(r.status_code)