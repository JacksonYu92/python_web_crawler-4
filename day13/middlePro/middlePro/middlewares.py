# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random
from scrapy.http import HtmlResponse

# 代理池:可以单独创建一个py文件，单独请求批量的代理ip，将其封装成列表的形式
proxy_list = [
    'ip1:port1','ip2:port2','ip3:port3',
]

class MiddleproDownloaderMiddleware:

    # 用来拦截/处理请求对象
    # 参数：
        #request: 拦截到的请求对象
    def process_request(self, request, spider):
        print('process_request函数被调用')
        #代理的设置
        # request.meta['proxy'] = 'https://ip:port'
        # 代理池应用
        request.meta['proxy'] = 'https:'+random.choice(proxy_list)
        #headers可以返回请求的请求头信息
        request.headers['User-Agent'] = 'xxx'
        #设置cookie
        request.headers['Cookies'] = 'xxx'
        return None

    # 用来拦截/处理响应对象
    #参数：
        #response：拦截到的响应对象
        #request：拦截到的响应对象所对应的请求对象
    def process_response(self, request, response, spider):
        print('process_response函数被调用')
        new_response = HtmlResponse(url=request.url, body="hello jackson", request=request, encoding='utf-8')
        print(new_response.text)
        print(spider.msg)
        return new_response
        # print(response.text)
        # return response

    # 用来拦截发生异常的请求对象
    #参数：
        #request：拦截到发生异常的请求对象
    #作用：拦截到异常的请求对象，需要对其进行修复，然后再次重新对其进行请求发送
    def process_exception(self, request, exception, spider):
        print('process_exception函数被调用',exception)
        #对异常的请求进行修复（进行代理的设置）

        #将发生异常的请求对象重新进行请求发送
        # return request
        pass