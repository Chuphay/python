import pattern, isEnglish
import tools as tls

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
        print "TypeError"
        return [word]    
    
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
def machine(text):
    temp = [i for i in text if i in ALPHA]
    text = "".join(temp)
    temp = text[:]
    words = text.split(" ")
    if text.islower():
        print "maybe we cracked this, here's what we got: "
        return text
    elif len(words) ==1:
        print "hmmm..."
        print text
        return text
    elif len(words) == 0:
        print "zero words?"
        return None    
    else:
        poss = possible(words[0])
        answer = []    
        for i in poss:
            #print words  
            new_word = i
            for k, letter in enumerate(new_word):
                text = text.replace(words[0][k],letter)
            words = text.split(" ")
            this_word = words[0]
            #print this_word 
            #print i, text
            try:
                rest = machine(" ".join(words[1:]))
                answer = this_word +" "+ rest
                if isEnglish.method(answer)>60:
                    print "ok... does this seem reasonable?"
                    return answer
                        
                else:
                    text = temp[:]
                    words = text.split(" ")
                    print "fail, but got here"
                   
            except Exception, e:
                print e
                print words, words[1:], this_word, rest
                exit()        

def method(text, percent = 70):
    temp = [i for i in text if i in ALPHA]
    text = "".join(temp)
    words = text.split(" ")
    for i, word in enumerate(words):
        poss = possible(word)
        for p in poss:
            temp = text[:]
            for k, letter in enumerate(p):
                temp = temp.replace(word[k],letter)
            new_words = temp.split(" ")
            total_words, errors = 0, 0    
            for j in range(i,len(new_words)):
                if new_words[j].islower():
                    print new_words[j], "is lower, continuing"
                    total_words +=1 
                    continue
                else:
                    print new_words[j], " is not lower" 
                    new_poss = possible(new_words[j])   


        


def main():
    text = """XHDQW... BKW FTRDN FUARBTWU. BKWXW DUW BKW YAIDMWX AF BKW XBDUXKTH WRBWUHUTXW. TBX QARBTRETRM PTXXTAR: BA WOHNAUW XBUDRMW RWL LAUNZX, BA XWWS AEB RWL NTFW DRZ RWL QTYTNTVDBTARX, BA CANZNI MA LKWUW RA ARW KDX MARW CWFAUW."""
    #print pattern.match("HGAAU")
    #zee =  possible("ADSFEBCGGHII")
    #print zee
    #print isEnglish.method("tails")>20
    test =  "ADSFEBCGGH taIGJ"
    #print machine(text)
    #print method(test)
    #print "abs gjkf".islower()
    #print possible("taJlI")
    test_text = tls.API(test)
    test_text.make(['ADSFE', '=','crlmn'])
    test_text.show()
    test_text.kill_all()
    test_text.show()
    
    
    
if __name__ == "__main__":
    main()    
