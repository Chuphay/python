from urllib2 import urlopen, URLError

class HTML(object):
    def __init__(self, url):
        self.url = url
        try:
            self.html = urlopen(url).read()
        except URLError:
            print "failed to open that url"
            self.html = ""
    def has(self,string):
       if string in self.html:
           return True
       else:
           return False 
    def getIndex(self, string):
        out = []
        index = 0
        while index < len(self.html):
            index = self.html.find(string, index)
            if index == -1:
                break
            out.append(index) 
            index += len(string)
        return out
    def getLinks(self):
        indexLinks = self.getIndex("<a href=")
        out = []
        for i in indexLinks:
            end = self.html.find(self.html[i+8],i+9)
            out.append(self.html[i+9:end])            
        return out    
                               
def main():            
    test= HTML("http://chuphay.github.io")
    print test.html
    print test.has("<a href=")
    print test.getIndex("<a href=")
    print test.getLinks()

if __name__ == "__main__":
    main()                
