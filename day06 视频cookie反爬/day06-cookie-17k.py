import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
login_url = 'https://passport.17k.com/ck/user/login'
data = {
    'loginName': 'loginName',
    'password': 'password'
}

session = requests.Session()
#请求的目的是为了获取cookie将其保存到session对象中
session.post(url=login_url, headers=headers, data=data)

#携带cookie向书架的页面进行请求发送，获取书架信息
#书架中的数据是动态加载的数据
book_url = 'https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919'
page_text = session.get(url=book_url, headers=headers).json()

print(page_text)