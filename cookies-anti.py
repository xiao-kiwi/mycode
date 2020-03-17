import requests
# from parsel import Selector
import pprint
from lxml import etree


url = 'http://www.porters.vip/verify/cookie/content.html'
headers = {
    "User-Agent" : "Postman",
    "Cookie":"isfirst=789kq7uc1pp4c"
}
resp = requests.get(url, headers=headers)
print(resp.status_code)
if resp.status_code == 200:
    html = etree.HTML(resp.text)
    res = html.xpath('/html/body/div[1]/div[2]/div/h1/text()')[0]
    # title = eval(res)
    pprint.pprint(res.strip())
else:
    print("失败")

'''
开始的请求头：
Host: www.porters.vip
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1

Host: www.porters.vip
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
'''
'''
后面的请求头：
Host: www.porters.vip
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Referer: http://www.porters.vip/verify/cookie/index.html
Connection: keep-alive
Cookie: isfirst=789kq7uc1pp4c
Upgrade-Insecure-Requests: 1
If-Modified-Since: Thu, 14 Mar 2019 08:31:11 GMT
If-None-Match: W/"5c8a114f-1695"
Cache-Control: max-age=0
'''