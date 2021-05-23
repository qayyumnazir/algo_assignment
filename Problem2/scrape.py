import requests
from bs4 import BeautifulSoup
url = "https://www.theedgemarkets.com/article/some-30-firms-negeri-sembilan-willing-buy-own-covid19-vaccine-says-state-executive"
r = requests.get(url)
#print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'post-content'})
#print(table.prettify())
p_tags = table.find_all('p')

for tag in p_tags:
    print(tag.get_text())

fileName = open('test.txt', "w")
fileName.write(tag.get_text())
fileName.close()



