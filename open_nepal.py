import requests
from parsel import Selector

url = "https://opendatanepal.com/api/trpc/dataset.search?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22query%22%3A%22%22%2C%22sort%22%3A%22score%20desc%2C%20metadata_modified%20desc%22%2C%22rows%22%3A10%2C%22start%22%3A0%2C%22groups%22%3A%5B%22energy-water-resources%22%5D%2C%22orgs%22%3A%5B%5D%2C%22tags%22%3A%5B%5D%2C%22resFormat%22%3A%5B%5D%2C%22facetsFields%22%3A%5B%22organization%22%2C%22tags%22%2C%22groups%22%2C%22res_format%22%5D%7D%7D%7D"

Headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-type": "application/json",
    "host": "opendatanepal.com",
    "referer": "https://opendatanepal.com/datasets?groups=energy-water-resources",
    "sec-ch-ua": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "trpc-accept": "application/jsonl",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
}
r = requests.get(url, Headers = Headers)
response = selector(r.text)
print(r.status_code)

json.str =response.xpath('//script[@id="__NEXT_DATA__"]/text()')
json_data = json.loads(json.str )
