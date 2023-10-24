import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
}
url = 'http://www.cip.cc/'

page_text = requests.get(url=url,headers=headers, proxies={'http':'223.109.206.226:4414'}).text
tree = etree.HTML(page_text)
text = tree.xpath('/html/body/div/div/div[3]/pre/text()')[0]
print(text.split('\n')[0])