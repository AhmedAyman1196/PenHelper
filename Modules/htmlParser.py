from bs4 import BeautifulSoup
from bs4 import Comment

import re
import requests

class hparser:
    def __init__(self, url):
        self.url = url
        self.resp = requests.get(url)

        # Done
        self.tags = [] # not unique , can be easily made unique
        self.links = []
        self.comments = []
        # to be done
        self.subs = [] # subdomains
        self.urls = [] # full urls
        self.domains = [] #full domains

        self.parse()

    def parse(self):
        soup = BeautifulSoup(self.resp.text , "lxml")
        self.tags = [tag.name for tag in soup.find_all()]
        self.links = [ link.get('href') for link in soup.find_all('a')]
        self.comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        #print([str(tag) for tag in soup.find_all()])
       # links = []
        # x = soup.find_all('a')
        # for i in x:
        #     s = i.attrs['href']
        #    # s = i.attrs['href'][:i.attrs['href'].index("cisco.com")]
        #     obj=re.compile(r'(http://|https://)(\w.+).')
        #     try:
        #         notexist=obj.search(s)
        #         links.append(notexist.group(2))
        #     except:
        #         x = 1
        # for i in links:
        #     print(i)







#print(resp.text)
