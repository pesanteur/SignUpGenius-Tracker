import requests
from bs4 import BeautifulSoup
import re

url = "http://www.signupgenius.com/index.cfm?go=s.signup&urlid=10c084baaa82da2fe3-term159&view=standard"

r = requests.get(url)

data = r.text
soup = BeautifulSoup(data, 'lxml')

#main_table = soup.find('td', attrs={'class': 'SUGmain'})
main_table = soup.find('table', attrs={'class': 'SUGtableouter'})

# main_table doesn't pull day of the week for some reason
# TODO: arrange table/list data by the day of the week that they are on

table_data = [[cell.text for cell in row('td')] for row in main_table('tr')]
# TODO: maybe simplify this, the table is not as complex as this thinks

test = [i.replace('\n', '').strip() for i in table_data[0]]
#TODO: add if statement to edit the following sample output
# ['Date (mm/dd/yyyy)', 'Time (AST)', 'Calendar View\t\t\t\tAvailable Slot']

# TODO: search first place in each list to check for date
date_regex = re.compile(r'ˆ\d{1,2}\/\d{1,2}\/\d{4}')
def find_date(data):
	date_regex = re.compile(r'^\d{1,2}\/d{1,2}\/\d{4}')
	search_date = date_regex.search(data)
	if search_date:
		return True

# TODO: Now use the above function to make a list in a list? 
