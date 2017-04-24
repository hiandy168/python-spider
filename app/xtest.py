from lxml import etree

# html = etree.parse('index.html')
html = etree.HTML('<html><head><title>test<body><h1>page title</h3>')
result = etree.tostring(html, pretty_print=True,method="html")

print(result)
