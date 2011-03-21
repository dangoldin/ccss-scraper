from BeautifulSoup import BeautifulSoup
import urllib, re

code_re = re.compile('\d+-\w+-\d+')

def getStandards(url):
	f = urllib.urlopen(url)
	soup = BeautifulSoup(f.read())
	#print soup.prettify()
	
	for li in soup.findAll('li'):
		#print li.prettify()
		for a in li.findAll('a'):
			if a.has_key('name') and code_re.search(a['name']):
				print a.prettify()

base_url = 'http://www.corestandards.org'
url = 'http://www.corestandards.org/the-standards/mathematics'

f = urllib.urlopen(url)
soup = BeautifulSoup(f.read())

#print soup.prettify()

for link in soup.findAll('a'):
	#print link.prettify()
	if '/the-standards/mathematics' in link['href']:
		print link['href']
		x = '/the-standards/mathematics/grade-4/operations-and-algebraic-thinking/'
		getStandards(base_url + x)
		exit()
		
