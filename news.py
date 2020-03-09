import requests
from parsel import Selector
import pprint

url = 'http://www.porters.vip/verify/uas/index.html'
headers = {
    "User-Agent" : "Postman"
}
resp = requests.get(url, headers=headers)
print(resp.status_code)
if resp.status_code == 200:
    sel = Selector(resp.text)
    res = sel.css('.list-group-item::text').extract()
    pprint.pprint(res)
else:
    print("失败")