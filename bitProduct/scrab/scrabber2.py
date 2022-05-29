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
    counts = r.html.find('span')
    # ali-kit_Link__secondary 
    lis = []
    prices = []
    sold = []
    categories_list = []
    count = 0
     
    for i in counts:
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('__resultsCount_'):
            count = i.text.replace('\n', '').replace('\t', '').replace('\r', '').split(' ')[0]
            count = count.replace('(', '').replace(')', '').replace(',' , '.')
            count = float(count)
            break
    for i in items: 
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('__name__'):
            lis.append(i.text)
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('snow-price_SnowPrice__blockMain'):
            price = i.text.replace('\n', '').replace('\t', '').replace('\r', '').split('.')[0]
            prices.append(price)
        #  
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('sold'):
            # take from string only numbers and input may be like (123)
            sold.append(i.text.replace('\n', '').replace('\t', '').replace('\r', '').split(' ')[0])
        
         
     
    return lis, prices, sold, count, categories_list


async def createApp(url, name):
    url = 'https://aliexpress.ru/wholesale?catId=&SearchText=' + name
    html = await get_html(url)
    products, prices, sold, count, categories_list = createContext(html)
    return products, prices, sold, count, categories_list


async def main(url, name):
    url = 'https://aliexpress.ru/wholesale?catId=&SearchText=' + name
    html = await get_html(url)
    products, prices, sold, count, categories_list = createContext(html)
    print(count)
    print(categories_list)
    if products:
        for product in range(len(products)):
            with open('products.csv', 'a', encoding='utf-8') as file:
                file.write(products[product] + ' | ' + prices[product] + " | " + sold[product] + '\n')
     


if __name__ == '__main__':
    asyncio.run(main(''))