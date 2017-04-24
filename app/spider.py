import urllib.request
from lxml import etree
import os

def getPages():
    baseUrl = 'http://www.mianfeiwendang.com/doc/083531eb169db5935bd01c1f/%d'

    urls = []

    for i in range(25):
        urls.append(baseUrl % (i + 1))

    # print(urls)
    return urls

def getPicLink(url):
    response = urllib.request.urlopen(url)

    html = response.read()
    html = etree.HTML(html)
    link = html.xpath('//p[@class="img"]/img/@src')

    return link

def downLoadPic(src):
    baseUrl = 'http://www.mianfeiwendang.com%s'
    
    src = baseUrl % src[0]
    # print(src)
    index = src.split('-')[0].split('/')[-1] + '.jpg'
    print(index)
    req = urllib.request.Request(src)
    response = urllib.request.urlopen(req)
    content = response.read()

    with open(index,'wb') as f:
        f.write(content)
        f.close()

if __name__ == '__main__':
    for link in getPages():
        downLoadPic(getPicLink(link))
