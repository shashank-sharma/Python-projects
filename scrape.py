'''

Scrape data and then plot graph.

'''

import requests
from bs4 import BeautifulSoup
import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np

na = []
arr_url = ["http://atc.ac.in/bottom-sidebar/cse/cse-faculty-member/","http://atc.ac.in/ec-faculty-member/","http://atc.ac.in/ce-faculty-member/","http://atc.ac.in/me-faculty-member/"]
for i in xrange(4):
	print 'Getting data ',i+1,'/4 :'
	url = arr_url[i]
	print '    Getting URL Request . . . ',
	r = requests.get(url)
	print '    Completed'
	soup = BeautifulSoup(r.content)
	table = soup.find_all("tr")
	arrx = []
	print '    Fetching Experience . . . ',
	for i in table:
		text = str(i)
		soupe = BeautifulSoup(text)
		text1 = soupe.get_text()
		num = [float(s) for s in text1.split() if s.replace('.','',1).isdigit()]
		if num:
			arrx.append(num[0])
		else:
			pass
	print '    Completed'
	print '\n'
	arrx = map(int,arrx)
	naa = np.array(arrx)                    #To count number of people with same experience
	naa = np.bincount(naa)
	naa = map(int,naa)
	na.append(naa)
print 'Plotting . . . '
CS = Bar(
    y=na[0],
    x=[q for q in range(0,33)]
)
EC = Bar(
    y=na[1],
    x=[q for q in range(0,33)]
)
CE = Bar(
    y=na[2],
    x=[q for q in range(0,33)]
)
ME = Bar(
    y=na[3],
    x=[q for q in range(0,33)]
)


data = Data([CS,EC,CE,ME])

py.iplot(data, filename = 'basic-line')

print '\n \n Completed'
