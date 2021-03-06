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
    links = r.html.find('a')
    
    # ali-kit_Link__secondary 
    lis = []
    prices = []
    solds = []
    link_list = []

    
    categories_list = []
    count = 0
    for i in links:
        if i.attrs.get('href') and i.attrs.get('href').startswith('//aliexpress.ru/store/'):
            attr = i.attrs.get('href')
            link = 'https://' + attr[2:]
            link_list.append(link)
             
    for i in counts:
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('__resultsCount_'):
            count = i.text.replace('\n', '').replace('\t', '').replace('\r', '').split(' ')[0]
            count = count.replace('(', '').replace(')', '').replace(',' , '.')
            count = count.split('.')
            count = count[0] + '.' + count[1]
            count = float(count)
            break
    for i in items: 
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('ProductSnippet__caption'):
            lis.append(i.text)
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('snow-price_SnowPrice__blockMain'):
            price = i.text.replace('\n', '').replace('\t', '').replace('\r', '').split('.')[0]
            price = price.replace('\xa0', '').replace(',','.').split(' ')[0]
            price = price.replace('(', '').replace(')', '')
            prices.append(price)
        #  
        if i.attrs.get('class') and i.attrs.get('class')[0].__contains__('sold'):
            # take from string only numbers and input may be like (123)
            sold = i.text.replace('\n', '').replace('\t', '').replace('\r', '').split(' ')[0]
            # replace ( )
            sold = sold.replace('(', '').replace(')', '')
            solds.append(sold)
         
    # calculate average of prices
    try:
        avg = 0
        for i in prices:
            avg += float(i)
        avg = avg / len(prices)
        avg = round(avg, 2)

        # calculate sum of sold
        sum_sold = 0
        for i in solds:
            sum_sold += float(i)
    except:
        sum_sold = 0
        avg = 0

    return lis, avg, sum_sold, count, categories_list, link_list


async def createApp(url, name):
    url = 'https://aliexpress.ru/wholesale?catId=&SearchText=' + name
    html = await get_html(url)
    products, prices, sold, count, categories_list, link_list = createContext(html)
    return products, prices, sold, count, categories_list, link_list


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