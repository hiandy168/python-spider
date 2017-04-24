import urllib.request
from lxml import etree

response = urllib.request.urlopen("http://www.mianfeiwendang.com/doc/083531eb169db5935bd01c1f/3")

html = response.read()
html = etree.HTML(html)
result = html.xpath('//p[@class="img"]/img/@src')

print(result)


# with open('cat_200_300.jpg','wb') as f:
#     f.write(cat_img)