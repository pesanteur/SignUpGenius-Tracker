import requests
from bs4 import BeautifulSoup

url = "http://www.signupgenius.com/index.cfm?go=s.signup&urlid=10c084baaa82da2fe3-term159&view=standard"

r = requests.get(url)

data = r.text
soup = BeautifulSoup(data, 'lxml')

#main_table = soup.find('td', attrs={'class': 'SUGmain'})
main_table = soup.find('table', attrs={'class': 'SUGtableouter'})
