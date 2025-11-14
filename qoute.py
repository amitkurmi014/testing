import requests
from parsel import Selector
import json

base_url = "https://quotes.toscrape.com/"
quote_d = []

page = 1                    

while True:

    url = f'{base_url}/page/{page}/'
    r = requests.get(url)
    response = Selector(r.text)

    data_quotes = response.xpath('//div[@class="quote"]')

    if not data_quotes:
        print("Empty page")
        break

    for data in data_quotes:
        qoute = data.xpath('.//span[@class="text"]/text()').get()
        author = data.xpath('.//small[@class="author"]/text()').get()
        image_url = data.xpath('.//span//a/@href').get()
        about = base_url + image_url
        tags = data.xpath('.//div/a[@class="tag"]/text()').getall()

        quote_data = {
            "Quote:": qoute,
            "Author:": author,
            "About_details:": about,
            "Tags:": tags
        }

        quote_d.append(quote_data)

    # move page increment OUTSIDE the loop
    page += 1
    print(r.status_code)

with open("quote.json", "w", encoding="utf-8") as q:
   json.dump(quote_d, q, ensure_ascii=False, indent=4)

    
