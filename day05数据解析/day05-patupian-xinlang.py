import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer':'https://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1'
}
url = 'https://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
img_src_list = tree.xpath('//*[@id="sina_keyword_ad_area2"]/div/a/img/@real_src')

data = requests.get(url=img_src_list[0], headers=headers).content

with open('1.jpg', 'wb') as fp:
    fp.write(data)