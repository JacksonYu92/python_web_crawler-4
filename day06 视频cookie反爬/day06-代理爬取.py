import requests
from lxml import etree
import random
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
}

#构建一个代理池（有很多不同的代理服务器）
proxy_url = 'http://webapi.http.zhimacangku.com/getip?num=80&type=3&pro=&city=0&yys=0&port=11&pack=337730&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
page_text = requests.get(url=proxy_url,headers=headers).text
proxy_list = [] #代理池
for ips in page_text.split('\n')[0:-1]:
    dic = {}
    dic['https'] = ips.strip()
    proxy_list.append(dic)

for page in range(1, 5001):
    print('正在爬取第%d页的ip数据......' % page)
    #生成不同页码对应的url
    url = 'https://www.kuaidaili.com/free/inha/%d/' % page
    page_text = requests.get(url=url, headers=headers,proxies=random.choice(proxy_list)).text
    time.sleep(1)
    tree = etree.HTML(page_text)
    ip = tree.xpath('//*[@id="list"]/div[1]/table/tbody/tr[1]/td[1]/text()')[0]
    print(ip)