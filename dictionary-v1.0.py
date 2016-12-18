'''
Personal Dictionary - v1.0

By - Shashank Sharma
Email - shashank.sharma98@gmail.com

'''
import requests
from bs4 import BeautifulSoup

def intro():
	print 'Welcome to Personal Dictionary - v1.0'
	print "Type 'search' to find meaning of any word"
	print "Type 'show' to get all saved words"
	print "Type 'show-meaning' to get all saved words meaning"
	print "Type 'exit' to quit"

# Show all words that are saved in database.
def words(comm):
    database = open("data.txt","r")
    ex = database.read().splitlines()
    database.close()
    print '\n\nTotal words found : ',len(ex)/2,'\n'
    s = 1
    if comm == 'show':
    	z = 2
    else:
    	z = 1
    for i in xrange(0,len(ex),z):
        print ex[i]

# Check if that word exist or not. If yes then show
def check_database(ex):
	co = 0
	for i in ex:
		if i == word:
			print ex[co+1]
			return True
		else:
			co+=1
	return False

# If word is not there then scrape it from internet and then save it.
def scrape(word):
    database = open("data.txt","a+")
    database.write("%s\n" % word)
    word = word.replace(' ','_')
    url = "http://yourdictionary.com/"+word
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    data = soup.find_all("div",{"class": "custom_entry"})
    for item in data:
        try:
            print item.contents[0].text
            database.write("%s\n" % (item.contents[0].text))
            break
        except:
            print item.text
            database.write("%s\n" % (item.text))
            break
    database.close()

intro()
while True:
	comm = raw_input()
	if comm == 'search':
		database = open("data.txt","r")
		ex = database.read().splitlines()
		database.close()
		print 'Enter word :',
		word = raw_input()
		found = check_database(ex)

		if not found:
			scrape(word)
	elif comm == 'show':
		words('show')
	elif comm == 'show-meaning':
		words('show-meaning')
	elif comm == 'help':
		intro()
	elif comm == 'exit':
		print '\n\n\nThank you for compiling me :P'
		break
	else:
		print "Having trouble ? Why don't you type again correctly"
		print "Type help to show commands again"