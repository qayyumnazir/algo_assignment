import requests
from bs4 import BeautifulSoup


#GDEX
#article 1

url = "https://www.theedgemarkets.com/article/gdex-partners-tasco-improve-logistics-delivery-services"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('gdex1.txt', "w")
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()

url = "https://www.theedgemarkets.com/article/gdex-ties-doc2us-alpro-pharmacy-ease-medication-delivery"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('gdex1.txt', "a")
fileName.write('\n' + 'article 2' + '\n')
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()

url = "https://www.theedgemarkets.com/article/gdex-look-creating-industrial-reit-part-next-growth-phase"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('gdex1.txt', "a")
fileName.write('\n' + 'article 3' + '\n')
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()
#end of GDEX's articles


#POS
"""
url = "https://www.theedgemarkets.com/article/new-courier-service-licence-freeze-positive-industry-—-experts"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('pos.txt', "w")
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()
r = requests.get(url)

url = "https://www.theedgemarkets.com/article/microlink-develop-insurance-renewal-digital-platform-pos-malaysia"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('pos.txt', "a")
fileName.write('\n' + 'article 2' + '\n')
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()

url = "https://www.theedgemarkets.com/article/mco-pos-malaysia-says-parcel-volume-rises-other-businesses-affected"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('pos.txt', "a")
fileName.write('\n' + 'article 3' + '\n')
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()
#End of POS
"""

#DHL
"""
url = "https://www.theedgemarkets.com/article/dhl-express-distributes-over-200-mil-vaccine-doses-internationally"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('dhl1.txt', "w")
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()

url = "https://www.theedgemarkets.com/article/dhl-predicts-strong-growth-b2b-ecommerce"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('dhl1.txt', "a")
fileName.write('\n' + 'article 2' + '\n')
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()

url = "https://www.theedgemarkets.com/article/tech-digitalisation-way-forward-dhl-express"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('dhl1.txt', "a")
fileName.write('\n' + 'article 3' + '\n')
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()
"""
#End of DHL

#Ninja van
"""
url = "https://www.theedgemarkets.com/article/ninja-van-capitalising-opportunities-presented-pandemic"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('ninja1.txt', "w")
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()

url = "https://www.theedgemarkets.com/article/australias-shippit-teams-ninja-van-serve-growing-ecommerce-market-malaysia"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('ninja1.txt', "a")
fileName.write('\n' + 'article 2' + '\n')
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()

url = "https://www.theedgemarkets.com/article/ninja-van-use-funds-raised-boost-malaysian-ops"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
p_tags = table.find_all('p')

fileName = open('ninja1.txt', "a")
fileName.write('\n' + 'article 3' + '\n')
for tag in p_tags:
    print(tag.get_text())
    fileName.write(tag.get_text() + "\n")
fileName.close()
"""


