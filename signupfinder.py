import requests
from bs4 import BeautifulSoup

url = "http://www.signupgenius.com/index.cfm?go=s.signup&urlid=10c084baaa82da2fe3-term159&view=standard"

r = requests.get(url)

data = r.text
soup = BeautifulSoup(data, 'lxml')

#main_table = soup.find('td', attrs={'class': 'SUGmain'})
main_table = soup.find('table', attrs={'class': 'SUGtableouter'})

# main_table doesn't pull day of the week for some reason
# TODO: arrange table/list data by the day of the week that they are on

test = [i.replace('\n', '').strip() for i in table_data[0]]
#TODO: add if statement to edit the following sample output
# ['Date (mm/dd/yyyy)', 'Time (AST)', 'Calendar View\t\t\t\tAvailable Slot']
