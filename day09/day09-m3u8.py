import requests
import os
import asyncio
import aiohttp
from threading import Thread
dirName = 'tsLib'
if not os.path.exists(dirName):
    os.mkdir(dirName)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

m3u8_file_url = 'https://cdn8.tvtvgood.com/202206/21/6abfb3237d01/playlist.m3u8?token=hh5wc-P-uYyeox1nfGkqsw&expires=1699147935'
m3u8_text = requests.get(url=m3u8_file_url, headers=headers).text
# print(m3u8_text)

ts_url_list = [] #存储解析出来的每一个ts片段的url
for line in m3u8_text.split('\n'):
    if not line.startswith('#'):
        ts_url = line
        ts_url = 'https://cdn8.tvtvgood.com/202206/21/6abfb3237d01/'+ts_url
        ts_url_list.append(ts_url)

#基于协程实现异步的ts片段的请求
async def get_request(url):#参数url就是ts片段的请求url
    async with aiohttp.ClientSession() as req:
        async with await req.get(url=url, headers=headers) as response:
            ts_data = await response.read()
            dic = {'ts_data':ts_data, 'ts_title': url.split('/')[-1]}
            return dic

def save_ts_data(t):
    dic = t.result()
    ts_data = dic['ts_data']
    ts_title = dic['ts_title']
    ts_path = dirName + '/' + ts_title
    with open(ts_path, 'wb') as fp:
        fp.write(ts_data)
    print(ts_title, ':保存下载成功！')

tasks = []
for url in ts_url_list:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(save_ts_data)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))


#使用协程：实现一定得有一个url列表，遍历该列表进行多协程的创建
#使用多个loop的场景：两种数据资源下载，需要实现有两个url列表
#问题：两个loop之间的关系是异步的吗?
#注意：千万别搞loop的嵌套。

#特殊的方式：创建两个线程，两个线程中封装处理两个loop。