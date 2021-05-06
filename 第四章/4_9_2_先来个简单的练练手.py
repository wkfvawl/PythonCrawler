import aiofiles
import aiohttp
import requests
import asyncio
import re
import os


# 获取m3u8的url
def get_m3u8_url(url, headers):
    resp = requests.get(url, headers=headers)
    obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取m3u8的url地址
    m3u8_url = obj.search(resp.text).group("url")  # 拿到m3u8的地址
    resp.close()
    return m3u8_url


# 下载m3u8文件
def download_m3u8_file(url, headers):
    resp = requests.get(url, headers=headers)
    with open("小舍得.m3u8", mode="wb") as f:
        f.write(resp.content)
    resp.close()
    print("下载完毕")


async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.ts", mode="wb") as f:
            await f.write(await resp.content.read())  # 把下载到的内容写入到文件中
    print(f"{name}下载完毕")


# 解析m3u8文件 异步下载
async def aio_download():
    tasks = []
    n = 1
    async with aiohttp.ClientSession() as session:  # 提前准备好session
        async with aiofiles.open("小舍得.m3u8", mode="r", encoding='utf-8') as f:
            async for line in f:
                line = line.strip()  # 去掉没用的空格和换行
                # line就是xxxxx.ts
                if line.startswith("#"):
                    continue
                task = asyncio.create_task(download_ts(line, n, session))  # 创建任务
                tasks.append(task)
                n = n + 1
            await asyncio.wait(tasks)  # 等待任务结束


def merge_ts():
    # mac: cat 1.ts 2.ts 3.ts > xxx.mp4
    # windows: copy /b 1.ts+2.ts+3.ts xxx.mp4

    os.system(f"copy /b *.ts> movie.ts")
    print("搞定!")


def main(url, headers):
    m3u8_url = get_m3u8_url(url, headers)
    print(m3u8_url)
    download_m3u8_file(m3u8_url, headers)
    # 异步协程
    asyncio.run(aio_download())  # 测试的使用可以注释掉
    # merge_ts()

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
    }
    url = "https://www.91kanju.com/vod-play/58988-1-1.html"
    main(url, headers)
