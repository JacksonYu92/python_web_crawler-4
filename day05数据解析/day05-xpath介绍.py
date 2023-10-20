from lxml import etree
#1. 创建一个etree类型的工具/对象,把被解析的页面源码数据加载到该对象中
tree = etree.parse('./test.html')
#2.调用etree对象的xpath函数，结合不同xpath表达式进行标签定位的数据提取
#标签定位的xpath表达式
#定位meta标签
# ret = tree.xpath('/html/head/meta')[0]
# ret = tree.xpath('//meta')[0] #从相对位置定位meta标签
#定位div标签
# ret = tree.xpath('//div')
#索引定位：想要定位到第一个div标签(下标是从1开始）
# ret = tree.xpath('//div[1]')
#属性定位：定位到class属性值为song的div标签：//tagName[@attrName="attrValue"]
# ret = tree.xpath('//div[@class="song"]')
#层级定位：定位所有li标签下的a标签
# ret = tree.xpath('//div[@class="tang"]/ul/li/a')
# ret = tree.xpath('//div[@class="tang"]//li/a')
# print(ret)

#数据提取：
    #提取标签内的文本内容
# ret = tree.xpath('//a[@id="feng"]/text()')#提取a标签中的文本内容
# ret = tree.xpath('//div[@class="song"]//text()')#提取div标签下所有的文本内容
#/text()提取标签直系的文本内容 //text()提取标签下所有的文本内容
# print(ret)
    #提取标签的属性值内容//tagName/@attrName
ret = tree.xpath('//img/@src')
print(ret)