from sys import argv
from tools import *

print """
Welcome to crack.py
 
Type q to quit at anytime 
Numbers will track how long it takes you to crack a code
If you need help, type help
"""   
i = 1
def response():
    global i
    prompt = '['+str(i)+'] '
    out = raw_input(prompt)
    out = out.split(' ')
    i+=1
    if out[0] == "q":
        exit() 
    elif out[0] == "help":
        print """
After you've loaded a text file to crack. 
You have 3 default options (obviously you can make more).
1a) 'show'  : this will show the text that you are working on
1b) 'show foo bar' : this assumes that you have made a module called tools
        In tools, the show function will call foo(bar(text))
        So for example, if you copied the top and letters definitions I supllied
        You can type 'show top10 letters' 
        and this will call 'tools.top10(tools.letters(text))'
1c) 'show library letters' : similar to the above, 
        If you made a global dictionary called library, 
        this'll call values from it
2) 'make TR = am' : this will change 'T' into 'a' and 
        'R' into 'm' in the text file
3) 'kill a' : if you make a mistake, then you can kill it. 
        'a' will turn back to 'R'.               
        """
        return True
    elif out[0] in dir(API):
        try:
            func = getattr(code,out[0])
            if len(out) == 1:
                return func()
            else:
                return func(out[1:])
        except NameError:
            print """Did you load in a text file to crack? 
You really have to do this first."""                    
    else:
        return out[0]

try:
    script, temp = argv
except ValueError:
    print "Which file do you want cracked?"
    temp = response()
while True:
    try:
        text = open(temp).read()
        global code
        code = API(text)
        print "Okay. Let's get crackin' on" , temp
        break
    except IOError:
        print """err... Couldn't open that file. 
Which file do you want cracked?"""
        temp = response()
    except TypeError:
        print """Which file do you want cracked?"""
        temp = response()      

while True:        
    do = response()
    if do == True:
        continue
    else:
        print """Didn't understand that. Please try again
or type 'help' for help, or 'q' to quit"""                 

