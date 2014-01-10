alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
craze = "LDCTFJUEBGQRWZAYKVNPOMHXSI"

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
#print e
import random        
message = list(ALPHA) 
random.shuffle(message)
message = ''.join(message)
print message        
       
