# 拿到页面源代码
# 提取和解析数据
import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# print(resp.text)

# 解析
html = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div")
for div in divs:  # 每一个服务商信息
    price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    com_name = div.xpath("./div/div/a[2]/div[1]/p/text()")[0]
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")[0]
    print(com_name)
