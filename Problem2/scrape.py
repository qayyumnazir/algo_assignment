import requests
from bs4 import BeautifulSoup
url = "https://www.theedgemarkets.com/article/some-30-firms-negeri-sembilan-willing-buy-own-covid19-vaccine-says-state-executive"
r = requests.get(url)
#print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
# table = soup.find_('div', attrs = {'id':'post-content'})
# print(table.prettify())
# text = []
# table.findAll('div', attrs = {'class':'field-item-even'})
soup.find_all('p')
print(soup.prettify())


