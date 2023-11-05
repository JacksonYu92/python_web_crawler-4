import asyncio
import time

async def get_request(url):
    print('正在请求的网址是：',url)
    time.sleep(2)
    print('请求网址结束')
    return 123

c = get_request('wwww.1.com')
# print(c)  #<coroutine object get_request at 0x000001FD8C8EF340>


task = asyncio.ensure_future(c)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)

