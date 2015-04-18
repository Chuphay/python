flat = open('flatland.txt').read()
pride = open('pride_and_prejudice.txt').read()
alice = open('alice_in_wonderland.txt').read()
carol = open('christmas_carol.txt').read()
text = flat + pride + alice + carol

alpha = "abcdefghijklmnopqrstuvwxyz "
def getWords(s):
    s = s.lower()
    lettersOnly = []
    english = []
    dict = {} 
    for i in s: 
        if i in alpha: 
            lettersOnly.append(i) 
    s = ''.join(lettersOnly) 
    s = s.split(" ")
    for i in s:
        try:
            dict[i] += 1
        except KeyError:
            dict[i] = 1
    del dict["enoughi"]
    for key in dict:
        if dict[key] > 2:
            english.append(key)
            
    return english
out = open('myDict.txt','w')
    
s = getWords(text)
s = " ".join(s)
out.write(s)
out.close()
   
        
    
