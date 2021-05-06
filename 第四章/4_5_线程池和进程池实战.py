# 1. 如何提取单个页面的数据
# 2. 上线程池,多个页面同时抓取
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)


def download_one_page(url):
    # 拿到页面源代码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # 去掉表头 下面两种方法都想
    # trs = table.xpath("./tr")[1:] # 从第1个开始 去掉第0个表头
    trs = table.xpath("./tr[position()>1]") # 位置大于1
    # 拿到每个tr
    for tr in trs:
        txt = tr.xpath("./td/text()") # tr中找td td中找文本
        # 对数据做简单的处理: \\  / 去掉
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        # 把数据存放在文件中
        csvwriter.writerow(txt)
    print(url, "提取完毕!")


if __name__ == '__main__':
    # for i in range(1, 14870):  # 效率及其低下
    #     download_one_page(f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")

    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):  # 199 * 20 = 3980
            # 把下载任务提交给线程池
            t.submit(download_one_page, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")

    print("全部下载完毕!")
