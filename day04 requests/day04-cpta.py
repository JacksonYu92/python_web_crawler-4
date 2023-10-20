import requests

url = 'http://www.cpta.com.cn/'

#User-Agent:请求载体（浏览器，爬虫程序）的身份标识
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
#伪装了浏览器的请求头
response = requests.get(url=url, headers=header)

page_text = response.text

with open('kaoshi.html', 'w') as fp:
    fp.write(page_text)

#程序模拟浏览器的力度不够