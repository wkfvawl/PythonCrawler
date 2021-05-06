# 案例2.抓取百度翻译数据
import requests

url = "https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的英文单词:")
dat = {
    "kw": s
}

# 发送post请求, 发送的数据必须放在字典中, 通过data参数进行传递
resp = requests.post(url, data=dat)
# 返回值是json 那就可以直接解析成json
# {'errno': 0, 'data': [{'k': 'Apple', 'v': 'n. 苹果公司，原称苹果电脑公司'}, {'k': 'apple', 'v': 'n. 苹果; 苹果公司; 苹果树'}, {'k': 'APPLE', 'v': 'abbr. applied parallel programming language 应用并行程序'}, {'k': 'apples', 'v': 'n. 苹果，苹果树( apple的名词复数 ); [美国口语]棒球; [美国英语][保龄球]坏球; '}, {'k': 'Apples', 'v': '[地名] [瑞士] 阿普勒'}]}
resp_json = resp.json()
print(resp_json['data'][0])  # 将服务器返回的内容直接处理成json()  => dict
resp.close()#关闭resp
