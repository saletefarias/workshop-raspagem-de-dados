from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'http://www.undb.edu.br/'
html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')
paragraph = soup.p
print(paragraph.text)
