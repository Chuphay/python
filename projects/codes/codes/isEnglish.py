temp = open("myDict.txt").read()
myDict = temp.split(" ")
alpha = "abcdefghijklmnopqrstuvwxyz "

def method(s):
    """method to return percent of words that are in myDict.txt"""
    s = s.lower()
    temp = []
    for i in s:
        if i in alpha:
            temp.append(i)
    s = "".join(temp)        
    s = s.split(" ")
    out = 0.0
    for i in s:
        if i in myDict:
            out +=1
    return 100*out/len(s)        
   
def main():
    txt2 = open("/home/chuphay/python/projects/codes/text/clueless.txt").read()
    txt = "Robots are your friends. Except for RX-686. She will try to eat you."
    print method(txt)>20
    print method(txt2)
    print txt

if __name__ =="__main__":
    main()    
