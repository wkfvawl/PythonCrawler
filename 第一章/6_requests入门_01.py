# 安装requests
# pip install requests
# 国内源
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
# 案例1. 抓取搜狗搜索内容
import requests
query = input("输入一个你喜欢的明星")

url = f'https://www.sogou.com/web?query={query}'

dic = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}

resp = requests.get(url, headers=dic)  # 处理一个小小的反爬

print(resp)#相应状态200
print(resp.text)  # 拿到页面源代码
resp.close()#关闭resp