import urllib
from bs4 import BeautifulSoup
print 'Welcome to Imager'
a=int(raw_input("Enter Number of Images to be scratched: --> "))
for i in range(0,a):
        web=urllib.urlopen('http://imgur.com/random')
	soup=BeautifulSoup(web)
	##soup.prettify()
        for link in soup.find_all('img'):
	       if(0==0):##loop breaker as url we are searching is the first to occur in web page
		       img=link.get('src')
		       break
        s='http:'
        img=s+img
        if "loader" in img: continue ## Filtering url
        print img
        urllib.urlretrieve(img, 'file'' '+ str(i+1) +'.jpg')##Can not concatenate 'string' object with 'int' thus use str(i)
