import asyncio
from pyppeteer import launch
from lxml import etree


async def get_data(url):
    # headless参数设为False，则变成有头模式
    browser = await launch(
        headless=False,
        # 可在浏览器中输入chrome://version/，在页面的"个人资料路径"查看浏览器的执行程序
        executablePath='C:\Program Files\Google\Chrome\Application\chrome.exe'
    )
    page = await browser.newPage()

    await page.goto(url)

    await asyncio.sleep(3)

    page_text = await page.content()

    await browser.close()
    return page_text


def parse(task):
    page_text = task.result()
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="data_row news_article clearfix "]')
    for div in div_list:
        title = div.xpath('.//div[@class="news_title"]/h3/a/text()')[0]
        print(title)


urls = ['https://news.163.com/domestic/',
        'https://news.163.com/world/',
        'https://war.163.com/']
tasks = []
for url in urls:
    c = get_data(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))