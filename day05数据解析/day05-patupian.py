import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
for page in range(1, 3):
    if page == 1:
        url = 'https://pic.netbian.com/4kfengjing/'
    else:
        url = f'https://pic.netbian.com/4kfengjing/index_{page}.html'
    #对首页进行页面源码数据的获取
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gbk'
    page_text = response.text
    #数据解析：图片的名字+详情页的url
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    # print(ul_list)
    for li in li_list:
        detail_url = 'https://pic.netbian.com' + li.xpath('./a/@href')[0]
        title = li.xpath('./a/b/text()')[0]
        # print(detail_url, title)
        #对图片详情页的url发起请求，获取详情页的页面源码数据

        detail_page_text = requests.get(url=detail_url, headers=headers).text
        #数据解析: 将详情页中的大图地址获取
        detail_tree = etree.HTML(detail_page_text)
        img_src = 'https://pic.netbian.com/'+detail_tree.xpath('//*[@id="img"]/img/@src')[0]
        # print(img_src)
        #对图片地址进行请求发送，下载图片
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = './imgs/' + title + '.jpg'
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        print(title, ': 保存下载成功！')