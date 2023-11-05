import requests
import os
from threading import Thread
from multiprocessing.dummy import Pool

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

dirName = 'tsLib'
if not os.path.exists(dirName):
    os.mkdir(dirName)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Connection':'closed'
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

def get_request(url):#参数url就是ts片段的请求url
    ts_data = requests.get(url=url, headers=headers, verify=False).content
    ts_path = dirName + '/' + url.split('/')[-1]
    with open(ts_path, 'wb') as fp:
        fp.write(ts_data)
    print(ts_path, ':保存下载成功！')

#HTTPSConnectionPool异常原因：
    #网络请求的并发量太大（减少并发，在headers中添加一个Connection：closed）

pool = Pool(100)
pool.map(get_request, ts_url_list)

