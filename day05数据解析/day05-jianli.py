import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
for page in range(1,2):#page的取值是1-5之间
    if page == 1:
        url = 'https://sc.chinaz.com/jianli/free.html'
    else:
        url = f'https://sc.chinaz.com/jianli/free_{page}.html'
    print(f'正在爬取第{page}页的数据......')
    #获取首页的页面源码数据

    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    #解析首页的页面源码数据：简历的名称+详情页的url
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//*[@id="container"]/div')
    for div in div_list:
        detail_url = div.xpath('./a/@href')[0]
        title = div.xpath('./p/a/text()')[0]
        # print(detail_url,title)
        #对详情页的url发起请求，获取详情页页面源码数据
        detail_response = requests.get(url=detail_url, headers=headers)
        detail_page_text = detail_response.text
        #对详情页进行数据解析：解析出下载地址
        detail_tree = etree.HTML(detail_page_text)
        download_url = detail_tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
        #对下载地址发起请求，下载对应的简历压缩包数据
        data = requests.get(url=download_url, headers=headers).content
        file_name = './jianli/' + title + '.rar'
        with open(file_name, 'wb') as fp:
            fp.write(data)

        print(title, ": 下载保存成功")