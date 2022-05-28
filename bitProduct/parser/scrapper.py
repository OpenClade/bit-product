from math import prod
import requests
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession



header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# request on wildberries.ru
 

# parse html
def get_content():
    ascession = AsyncHTMLSession()
    ascession.headers = header
    r = ascession.get(html.url)
    soup = BeautifulSoup(html.content)
    #  print all classed with div
     
    items = soup.find('div')
    lis = []
    for i in items:
        print(i)
        if i.get('class').__contains__('SearchProductFeed_ProductSnippet__name__'):
            lis.append(i.text)     

    return lis


# write to file
def write_csv(data):
    with open('products.csv', 'a') as file:
        file.write(data + '\n')


# main function
def main():
    url = 'https://aliexpress.ru/wholesale?catId=&SearchText=компьютер'
    html = get_html(url) 
    products = get_content(html)
    if products:
        for product in products:
            write_csv(product)
    print(products)
if __name__ == '__main__':
    main()
