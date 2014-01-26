def method(word):
    word = word.lower()
    poss = "0123456789ABCDEFGHIJKL"
    position = 0
    out = []
    temp = {}
    for i in word:
        if i in temp:
            out.append(temp[i])
        else:
            out.append(poss[position])
            temp[i] = poss[position]
            position += 1
    return "".join(out)  

myDict = open("myDict.txt").read()
myDict = myDict.split(" ")
patterns = {}
for i in myDict:
    z = method(i)
    try:
        patterns[z].append(i)
    except KeyError:
        patterns[z] = [i]            

def match(word):
    pattern = method(word)
    if pattern in patterns:
        return patterns[pattern]
    else:
        print "no match for ", word 
        return None   
    

def main():
    word = "classification"            
    print method(word)
    print match("HGHHU")
    
if __name__ == "__main__":
    main()       
        
    
