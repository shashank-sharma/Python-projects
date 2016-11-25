import requests
from bs4 import BeautifulSoup
print 'Getting Data from site . . .',
url = "http://atc.ac.in/bottom-sidebar/cse/cse-faculty-member/"
r = requests.get(url)
flag = 0
print 'Completed'
soup = BeautifulSoup(r.content)
table = soup.find_all("tr")
print 'Enter name:  ',
inp = raw_input()
for i in table:
	try:
		text = i.contents[3]
	except:
		pass
	text = str(text)
	try:
		soupe = BeautifulSoup(text)
		if inp in soupe.get_text():
			print '-----------------'
			print 'Result Found'
			print '-----------------'
			flag = 1
	except:
		print 'Error'
	if flag == 1:
		print(soupe.get_text())
		if text == '<td></td>':
			flag = 0