# 安装
# pip install bs4 -i 清华

# 1. 拿到页面源代码
# 2. 使用bs4进行解析. 拿到数据
import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)

f = open("菜价.csv", mode="w")
csvwriter = csv.writer(f)

# 解析数据
# 1. 把页面源代码交给BeautifulSoup进行处理, 生成bs对象
# html.parser 告诉解析器这是html文件
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
# 2. 从bs对象中查找数据
# find(标签, 属性=值)
# find_all(标签, 属性=值)
# table = page.find("table", class_="hq_table")  # class是python的关键字
table = page.find("table", attrs={"class": "hq_table"})  # 和上一行是一个意思. 此时可以避免class
# 拿到所有数据行tr
# 行tr 列td
print(table)
#做切片 从第一个开始切 排除了第0个表头 获得纯数据
trs = table.find_all("tr")[1:]
for tr in trs:  # 每一行
    tds = tr.find_all("td")  # 拿到每行中的所有td
    name = tds[0].text  # .text 表示拿到被标签标记的内容
    low = tds[1].text  # .text 表示拿到被标签标记的内容
    avg = tds[2].text  # .text 表示拿到被标签标记的内容
    high = tds[3].text  # .text 表示拿到被标签标记的内容
    tp = tds[4].text  # .text 表示拿到被标签标记的内容
    kind = tds[5].text  # .text 表示拿到被标签标记的内容
    date = tds[6].text  # .text 表示拿到被标签标记的内容
    csvwriter.writerow([name, low, avg, high, tp, kind, date])

f.close()
print("over1!!!!")


