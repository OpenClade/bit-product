import requests
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import asyncio

async def get_html(url):
    session = AsyncHTMLSession()
    r = await session.get(url)
    # await r.html.arender()
    return r


def createContext(r): 
    r.html.find('div', first=True)
    items = r.html.find('div')
    lis = []
    prices = []
    sold = []
    for i in items: 
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('__name__'):
            lis.append(i.text)
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('snow-price_SnowPrice__blockMain'):
            prices.append(i.text.replace('\n', '').replace('\t', '').replace('\r', '').split('.')[0])
        #  
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('sold'):
            # take from string only numbers and input may be like (123)
            sold.append(i.text.replace('\n', '').replace('\t', '').replace('\r', '').split(' ')[0])
 
     
    return lis, prices, sold


async def createApp(url):
    html = await get_html(url)
    products, prices = createContext(html)
    return products, prices 


async def main(url):
    url = 'https://aliexpress.ru/wholesale?catId=&SearchText=компьютер'
    html = await get_html(url)
    products, prices, sold = createContext(html)
     
    if products:
        for product in range(len(products)):
            with open('products.csv', 'a', encoding='utf-8') as file:
                file.write(products[product] + ' | ' + prices[product] + " | " + sold[product] + '\n')
    print(products)


if __name__ == '__main__':
    asyncio.run(main(''))