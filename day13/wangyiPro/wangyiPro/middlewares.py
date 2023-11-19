# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from time import sleep
from scrapy.http import HtmlResponse

class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):
        model_url_list = spider.model_url_list
        if request.url in model_url_list:
            bro = spider.bro
            bro.get(request.url)
            sleep(2)
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            page_text = bro.page_source
            new_response = HtmlResponse(url=request.url,body=page_text,request=request,encoding='utf-8')
            return new_response
        return response

    def process_exception(self, request, exception, spider):

        pass
