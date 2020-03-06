import requests
from parsel import Selector


url = 'https://www.vmall.com/product/10086763808943.html?cid=99844'
resp = requests.get(url)
# print(resp.text)
sel = Selector(resp.text)
res = sel.css('#pro-name::text').extract()
print(res)