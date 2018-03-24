from urllib.request import urlopen
url = 'http://www.worldatlas.com/articles/the-25-largest-internet-companies-in-the-world.html'
html = urlopen(url)
print(html.read())
