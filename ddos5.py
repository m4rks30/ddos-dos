import requests
import asyncio
import aiohttp
async def send_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(await response.text())

async def send_multiple_requests(urls):
    tasks = []
    for url in urls:
        tasks.append(asyncio.ensure_future(send_request(url)))
    await asyncio.gather(*tasks)

urls = ['https://google.com']
loop = asyncio.get_event_loop()
loop.run_until_complete(send_multiple_requests(urls))
