from bs4 import BeautifulSoup

import re
import requests

class hparser:
    def __init__(self, url):
        self.url = url
        self.resp = requests.get(url)


    def parse(self):
        soup = BeautifulSoup(self.resp.text , "lxml")
        links = []
        x = soup.find_all('a')
        for i in x:
        	if "cisco.com" in i.attrs['href'] :
        		s = i.attrs['href'][:i.attrs['href'].index("cisco.com")]
        		obj=re.compile(r'(http://|https://)(\w.+).')
        		#print(type(s))
        		try:
        			notexist=obj.search(s)
        			#print(s)
        			links.append(notexist.group(2))
        		except:
        			print("\n")
        for i in links:
        	print(i)
        print(len(links))






#print(resp.text)
