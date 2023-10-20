import requests

url='https://www.xiachufang.com/search/'
keyword = input('Please input shicai: ')
param = {
    'keyword': keyword,
}
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
response = requests.get(url=url,params=param, headers=header)
page_text = response.text

with open(f"{keyword}.html", "w") as fp:
    fp.write(page_text)