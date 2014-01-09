alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
'o','p','q','r','s','t','u','v','w','x','y','z']
ALPHA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',\
'O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(s,key):
    s = s.replace("\n", "")
    s = s.lower()
    output = ""
    for i in s:
        try:
            j = (alpha.index(i)+key)%len(alpha)
            output += ALPHA[j]
        except ValueError:
            output += i 
    if key<0:
        output = output.lower()
        return output
    else:           
        return output
jedi = open("/home/chuphay/python/projects/codes/text/jedi.txt").read()
e = encrypt(jedi,1)
print e        
       
