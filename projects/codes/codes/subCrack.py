import pattern, isEnglish

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

def possible(word):
    temp = pattern.match(word)
    try:
        copy = temp[:]
        for i, letter in enumerate(word):
            if letter.islower() == True:
                for j in temp:
                    if j[i] == letter:
                        continue
                    else:
                        try:
                            copy.remove(j)
                        except ValueError:
                            pass             
    
        return copy
    except TypeError:
        #print "TypeError"
        return [word]

def transform(word, seed, text):
    """word is generally upper case, seed is lower case, text is the full text.
    a text will be returned with all the changes made."""
    for k, letter in enumerate(seed):
        text = text.replace(word[k],letter)
    return text  
    
def checkForEnglish(text, number, percent):
    """text is the text we are checking, number is the number of words already transformed.
    percent is the percent that is desired to be english. 
    note that if 70% is the percent, 
    it will fail whenever the first n = number of words are only 70% english
    Basically this is the UI for this program,
    If it fails, it will return True
    If it is english, it'll ask, 
    if it seems like english to the user, then the system will exit
    else, it just returns False. 
    """
    #first, we simply say False if the number is too small
    if number<2:
        return False
    #next, we split up the words
    temp = [i for i in text if i in ALPHA]
    temp = "".join(temp)
    words = temp.split(" ")
    words = words[:number]
    sentence = " ".join(words)
        
    #next we check for fail

    failCheck = isEnglish.method(sentence)  
    failPercent = 100 - percent
    print round(failCheck), text[:60]
    if failCheck< 50:
        return True
    #next we check to see if it is English
    check = isEnglish.method(text)
    if check>=percent:
        print "hmm... possible crack. does this look right?"
        print text
        answer = raw_input("y/n: ")
        if answer == "y":
            exit()
        else:
            return True
                   
    #the default case, is basically False, keep on cracking
    return False            
                

def machine(text, percent = 65, recursion = 0):
    """Starting over again for the fourth time
    This method will return a cracked version of a simple substitution cipher if it finds it.
    It operates on an ecrypted text.
    It counts how many recursion levels, you are on
    and, from this, it will know which word to seed
    The percent input, is defaulted at 60%.
    It uses recursion to decrypt the text.
    checking at each step if it is english yet.
    If, after one cycle through, starting from the first word, it doesn't find English
    It will then, move the first word to the end of the list and start again on the second word.
    After trying all words, it will break out of the recursion cylce.
    scratch that, that should be user implemented
    """ 
    #obviously first we make our word list 
    
    temp = [i for i in text if i in ALPHA]
    temp = "".join(temp)
    words = temp.split(" ")
    #we put in a base case
    #my feeling is that we wont be getting here too often, but let's see how it goes
    if len(words) == recursion:
        pass
        #print possible(text)
    else:
        #then we find the possibilities
        possibilities = possible(words[recursion])
        if possibilities == []:
            machine(text,percent,recursion+1)
        else:    
            #we will loop over all possibilities, calling them the seed
            for seed in possibilities:
                if seed.islower():
                            
                    #first we transform our text into a new text
                    new_text = transform(words[recursion],seed,text)
                    #we send a recursive call on the next set of words
                    #recursion +=1
                    machine(new_text,percent,recursion+1)
                    #I think before sending a recursive call, let's check for english
                    if checkForEnglish(new_text, recursion, percent):
                        continue
                else:
                    machine(text,percent,recursion+1)         

    pass

def method(text,percent=65):
    """here's are main method. basically
    it'll just be calling the machine function, but in case
    the machine returns None, then it will shift the first word, to the end of the text file"""
    answer = machine(text,percent)
    if answer == None:
        print "hmm... try without the first word?"
        print text
        answer = raw_input("y/n: ")
        if answer == "n":
            exit()
        else:
            
            temp = [i for i in text if i in ALPHA]
            temp = "".join(temp)
            words = temp.split(" ")
            sentence = " ".join(words[1:]) 
            method(sentence,percent)
             

    


def main():
    print "working...."
    text = """spDQW... BKW FTRDN FUARBTWU. BKWXW DUW BKW YAIDMWX AF BKW XBDUXKTH WRBWUHUTXW. TBX QARBTRETRM PTXXTAR: BA WOHNAUW XBUDRMW RWL LAUNZX, BA XWWS AEB RWL NTFW DRZ RWL QTYTNTVDBTARX, BA CANZNI MA LKWUW RA ARW KDX MARW CWFAUW."""
    text2 = """XHDQW... BKW FTRDN FUARBTWU. BKeXe aUe BKe""" 

    #print pattern.match("HGAAU")
    #zee =  possible("ADSFEBCGGHII")
    #print zee
    test =  "ADSFEBCGGH FSIGJ"
    test2 = "ADSFEBCGGH taIGJ"
    test3 = 'this is some example text to do a cipher on'
    test4 = 'ESTD TD DZXP PILXAWP EPIE EZ OZ L NTASPC ZY'
    #print "abs gjkf".islower()

    print method(text)
    #print transform('FSIGJ', 'table', test)
    #print checkForEnglish(test2, 2, 60)
    #print checkForEnglish(test3, 2 ,60)
    #print isEnglish.method("into to omit tIoiAWt itIi im am o NtAntC mY")

#print globals()
    
    
if __name__ == "__main__":
    main()    
