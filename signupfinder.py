import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict

url = "http://www.signupgenius.com/go/10c084baaa82da2fe3-term162"

r = requests.get(url)

# TODO: Add tests so we don't have to rewrite
data = r.text
soup = BeautifulSoup(data, 'lxml')

""""The following class allows us to append to an OrderedDict"""
class MyOrderedDict(OrderedDict):
	def append(self, key, value):
		root = self._OrderedDict__root
		last = root[0]

		if key in self:
			raise KeyError
		else:
			root[0] = last[1] = self._OrderedDict__map[key] = [last, root, key]
			dict.__setitem__(self, key, value)



#main_table = soup.find('td', attrs={'class': 'SUGmain'})
main_table = soup.find('table', attrs={'class': 'SUGtableouter'})

# main_table doesn't pull day of the week for some reason
# TODO: arrange table/list data by the day of the week that they are on

table_data = [[cell.text for cell in row('td')] for row in main_table('tr')]
# TODO: maybe simplify this, the table is not as complex as this thinks
# TODO: this code duplicates some information from the table...possibly due to the merge structure of the initial column

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
	if date_regex is not  None:
		return True
	else:
		return False

list_for_dates = [] # Use a better variable name
sub_list = []

count = 0 # Useful to track number of cells without date, so we know what to add to first occuring date

for i in range(len(table_data)): # Maybe just use table_first up top?
	cell_1 = table_data[i][0]
	if find_date(cell_1):
		list_for_dates.append(cell_1)
	
print(list_for_dates) # For now

# Test logic, TODO: use a ordered dictionary instead of a list of lists
big_list = []
inner_list = []



if find_date(table_data[1][0]): # iterate over the first position with a for loop
	big_list.append(table_data[1][0])
	inner_list.append(table_data[1][1:])
	d = OrderedDict([(big_list, inner_list)])
	# Append to MyOrderedDict using class
	d.append() # Ordering is messed up here figure this out
