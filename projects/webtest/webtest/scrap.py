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
            #have to check for both types of quotes: ' , "
            #and then take the smaller of the two
            end = self.html.find("'",i+9)
            end_other = self.html.find('"',i+9)
            if end == -1:
                end = end_other
            if end_other == -1:
                end_other = end
            if end>end_other:
                end = end_other
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
