from BeautifulSoup import BeautifulSoup
import urllib, re, time, sys, random

code_re = re.compile('\d+-\w+-\d+')
code_re2 = re.compile('-.+-\d+')
base_url = 'http://www.corestandards.org'
url = 'http://www.corestandards.org/the-standards/mathematics'

SLEEP_TIME = 2

class CCSS:
	def getStandards(self,url):
		time.sleep( SLEEP_TIME + random.randint(0,SLEEP_TIME) )
		f = urllib.urlopen(url)
		soup = BeautifulSoup(f.read())
		#print soup.prettify()
		
		data = []
		for li in soup.findAll('li'):
			#print li.prettify()
			for a in li.findAll('a'):
				if a.has_key('name') and (code_re.search(a['name']) or code_re2.search(a['name'])):
					#print a.prettify()
					code = a['name']
					text = li.text
					data.append( (code, text.encode('utf-8')) )
					print code,':',text.encode('utf-8')
		return data

	def getLinks(self,url):
		f = urllib.urlopen(url)
		soup = BeautifulSoup(f.read())

		#print soup.prettify()

		data = []
		for link in soup.findAll('a'):
			#print link.prettify()
			if '/the-standards/mathematics' in link['href']:
				print 'Getting',base_url + link['href']
				code_info = self.getStandards(base_url + link['href'])
				data.extend(code_info)
				
		return data
		
ccss = CCSS()
codes = ccss.getLinks(url)

f = open(sys.argv[1], 'w')
f.write("code\ttext\n")
for code_info in codes:
	f.write("%s\t%s\n" % (code_info[0], code_info[1]))
f.close()