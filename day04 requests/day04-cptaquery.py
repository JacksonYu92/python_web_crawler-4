import requests

url = 'http://www.cpta.com.cn/category/search'
param = {
    'keywords': '人力资源',
     '搜 索': '搜 索',
}
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
#发起了post请求：通过data参数携带了请求参数
response = requests.post(url=url, data=param, headers=header)

page_text = response.text

with open('renshi.html', 'w') as fp:
    fp.write(page_text)

#通过抓包工具定位了指定的数据包：
    #提取：url，请求方式，请求参数，请求头信息
