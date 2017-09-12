import requests
from bs4 import BeautifulSoup
import re

url = "http://www.signupgenius.com/go/10c084baaa82da2fe3-term162"

r = requests.get(url)

# TODO: Add tests so we don't have to rewrite
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
	if search_date.group():
		return True

# TODO: Now use the above function to make a list in a list? 
# TODO: Add the following lists without a date feature to this date

table_first = [item[0] for item in table_data] # gets the first item in the sublist BUT we want to iterate over this and pull all dates 

def find_date(data):
	""""Checks whether content of a cell is a date"""
	date_regex = re.match(r'^\d{1,2}\/\d{1,2}\/\d{4}', data)
	if data_regex is not  None:
		return True
	else:
		return False

list_for_dates = [] # Use a better variable name
count = 0 # Useful to track number of cells without date, so we know what to add to first occuring date

for i in range(len(table_data)):
	cell_1 = table_data[i][0]
	if find_date(cell_1):
		list_for_dates.append(cell_1)
	print(i) # For now
