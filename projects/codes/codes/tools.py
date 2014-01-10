import frequency as tools

class API(object):
    """This is the default command line API"""
    def __init__(self,text):
        self.text = text
        self.dict = {}
    def make(self, x = 0):
        try:
            for i, e in enumerate(x[0]):
                if x[2][i] in self.dict:
                    print "You've already made",self.dict[x[2][i]], "=", x[2][i]
                else:    
                    self.dict[x[2][i]] = e
                    self.text = self.text.replace(e,x[2][i])
            return True
        except IndexError:
            print "Correct syntax is 'make T = a' or 'TR = ae', etc."
            return True     
    def kill(self, x = 0):
        try:
            for i in x[0]:
                self.text = self.text.replace(i,self.dict[i])
                del self.dict[i]
            return True
        except TypeError:
            print "Correct syntax is 'kill a' or 'kill ae'."
            return True
        except KeyError:
            print "err... remember, kill lower case things you've already made."       
    def show(self, x = 0):
        if x == 0:
            print self.text 
            return True
        else:
            try: 
                if x[0] == 'library':
                    print tools.library[x[1]]
                    return True
                else:    
                    print getattr(tools,x[0])(getattr(tools,x[1])(self.text))
                    return True
            except AttributeError:
                print """hmmm... Did you define that in the tools module.
                Correct syntax is 'show' to see the text,
                'show top10 letters' or 'show library letters', etc.
                If you are having massive problems with this.
                Please ask Dave for help."""
                return True
