import requests
from parsel import Selector
import json


oxy_d = []

for i in range(1,95):
    url = f'https://sandbox.oxylabs.io/products?page={i}'

    r = requests.get(url)
    response = Selector(r.text)

    json_str= response.xpath('.//script[@id="__NEXT_DATA__"]/text()').get()
    joson_data = json.loads(json_str)
    products = joson_data.get('props').get('pageProps').get('products')

    rates = {
        "A":1,
        "B":2,
        "C":3,
        "D":4,
        "E":5,
    }

    for product in products:
        title = product.get('game_name')
        description = product.get('description')
        url = product.get('url')
        genre = product.get('genre')
        rate_letter = product.get('rating')
        rate_value = rates.get(rate_letter,None)
        instock = product.get('inStock')
        if instock:
            instock="In of Stock"
        else:
            instock="Out of Stock"

        type = product.get('type')


        oxy_data= {
                "Title": title,
                "Description": description,
                "Genre": genre,
                "Rating Value": rate_value,
                "Stock": instock,
                "Type": type
        }
        oxy_d.append(oxy_data)


    print(r.status_code)
    print(f'{i} completed')

with open("oxy.json","w",encoding="utf-8") as f:
    json.dump(oxy_d,f,indent=4,ensure_ascii=False)