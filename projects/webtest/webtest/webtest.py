from urllib2 import Request, urlopen, URLError
from sgmllib import SGMLParser
'''
#request = Request('http://placekitten.com/')
#request = Request('http://www.codecademy.com/')
#request = Request('http://learnpythonthehardway.org/book/ex51.html')
request = Request('http://chuphay.github.io/finance.html')

try:
	response = urlopen(request)
	kittens = response.read()
	#print kittens[559:1000]
	print kittens
except URLError, e:
    print 'No kittez. Got an error code:', e
'''
sock = urlopen("http://chuphay.github.io/finance.html")
htmlSource = sock.read()
print htmlSource  

class URLLister(SGMLParser):
    """I got this from diveintopython.net""" 
    def reset(self):                              
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):                     
        href = [v for k, v in attrs if k=='href'] 
        if href:
            self.urls.extend(href) 

parser = URLLister()
parser.feed(htmlSource)         
sock.close()                     
parser.close() 
                 
for url in parser.urls: 
    print "you have succesfully parsed one <a href = '"+url+"'"
                
