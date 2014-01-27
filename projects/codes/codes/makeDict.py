text1 = open("/home/chuphay/python/projects/codes/text/clueless.txt").read()
text2 = open("/home/chuphay/python/projects/codes/text/obama.txt").read()
text3 = open("/home/chuphay/python/projects/codes/text/alice_in_wonderland.txt").read()
text4 = open("/home/chuphay/python/projects/codes/text/christmas_carol.txt").read()
text5 = open("/home/chuphay/python/projects/codes/text/flatland.txt").read()
text6 = open("/home/chuphay/python/projects/codes/text/pride_and_prejudice.txt").read()

text = text1+text2+text3+text4+text5+text6

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
    del dict["ab"]
    del dict["st"]
    del dict["o"]
    del dict["b"]
    del dict["c"]
    del dict["e"]
    del dict["f"]
    del dict["m"]
    del dict["w"]
    del dict["d"]
    del dict["contralto"]
    del dict["chromatistes"]
    del dict["christmasand"]
    del dict["cratchits"]
    del dict["cratchit"]
    del dict["herbut"] 
    del dict["herelizabeth"] 
    del dict["heri"]  
    del dict["herselfmrs"] 
    del dict["herselfshe"] 
    del dict["hertfordshire"] 
    del dict["herwhen"] 
    del dict["ini"]
    del dict["itand"] 
    del dict["iti"] 
    del dict["itit"]
    del dict["itmr"] 
    del dict["itmy"] 
    del dict["itthe"] 
    del dict["itthey"] 
    del dict["ityou"]
    del dict["nowi"]

    
    for key in dict:
        if dict[key] > 2:
            english.append(key)
    english += ["plastic","robot","groovy"]
    english = sorted(english)        
    return english

out = open('myDict.txt','w')
    
s = getWords(text)
print len(s)

s = " ".join(s)
out.write(s)
out.close()
