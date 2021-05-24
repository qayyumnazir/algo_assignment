import requests
from bs4 import BeautifulSoup


#GDEX
url = "https://www.theedgemarkets.com/article/gdex-partners-tasco-improve-logistics-delivery-services"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('gdex.txt', "w")
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()



