import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.setViewport({'width':width, 'height':height})

asyncio.get_event_loop().run_until_complete(main())