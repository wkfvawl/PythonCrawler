# 案例3: 抓取⾖瓣电影
import requests

url = "https://movie.douban.com/j/chart/top_list"

# url ="https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"
# url参数过长，使用第二种方式来封装参数

# 重新封装参数 字典
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
#get 请求参数params
resp = requests.get(url=url, params=param, headers=headers)

print(resp.json())
resp.close()#关闭resp