import requests
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import asyncio

async def get_html(url):
    # session = AsyncHTMLSession()
    # r = await session.get(url) 
    # await r.html.arender()
    # open browser and get html
    
    return r


def createContext(r): 
    r.html.find('div', first=True)
    items = r.html.find('span')
    print(r.html.links)
    print(items)
    return items


async def createApp(url):
    html = await get_html(url)
    products, prices = createContext(html)
    return products, prices 


async def main(url):
    url = 'https://kz.wildberries.ru/catalog/0/search.aspx?sort=popular&search=часы'
    html = await get_html(url)
    items = createContext(html)
    print(items)

     

if __name__ == '__main__':
    asyncio.run(main(''))