import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
#对首页进行页面数据请求
url = 'https://bixuejian.5000yan.com/'
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text
# print(page_text)
#数据解析：解析章节的标题&详情页的url
tree = etree.HTML(page_text)
#li_list列表中存储的是xpath表达式定位到的每一个li标签
li_list = tree.xpath('/html/body/div[2]/div[1]/main/ul/li')
# li_list = tree.xpath('//ul[@class="paiban"]//a//text()')
# print(li_list)

fp = open('xiaoshuo.txt', 'w')

for li in li_list:
    #局部解析：只可以解析li标签内部的局部标签
    title = li.xpath('./a/text()')[0]# 这个.表示的xpath的调用者，也就是li标签
    detail_url = li.xpath('./a/@href')[0]
    # print(title,detail_url)
    #对详情页的url发起请求，获取详情页的页面源码数据
    detail_response = requests.get(url=detail_url, headers=headers)
    detail_response.encoding = 'utf-8'
    detail_page_text = detail_response.text
    #对详情页进行数据解析：章节内容
    detail_tree = etree.HTML(detail_page_text)
    content = detail_tree.xpath('/html/body/div[2]/div[1]/main/section/div[1]//text()')
    #将content列表转换成一个完整的字符串
    content = ''.join(content).strip()
    # print(content)
    #持久化存储
    fp.write(title+':'+content+'\n')
    print(title,':章节下载保存成功！')
fp.close()