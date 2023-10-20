import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer':'https://sc.chinaz.com/'
}
url = 'https://sc.chinaz.com/tupian/taikongkexuetupian.html'
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text
tree = etree.HTML(page_text)
div_list = tree.xpath('/html/body/div[3]/div[2]/div')

for div in div_list:
    img_url = 'https://sc.chinaz.com' + div.xpath('./div/a/@href')[0]
    title = div.xpath('./div/a/text()')[0]
    # print(title, img_url)
    detail_page_text = requests.get(url=img_url, headers=headers).text
    detail_tree = etree.HTML(detail_page_text)

    detail_img_url = 'https:'+detail_tree.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[2]/img/@src')[0]
    # print(detail_img_url)
    img_data = requests.get(url=detail_img_url, headers=headers).content
    img_path = './newimgs/'+ title + '.jpg'
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
    print(title, ': 保存下载成功！')
