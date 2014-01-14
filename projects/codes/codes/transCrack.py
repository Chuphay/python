import isEnglish
import transDecrypt as td

def main():
    text = """alr oonl huu  ao rakwufpearrpey olp.wme  i  talfah le eb ed ekladeeiyoren c pgwta  ionys"""
    method(text,50)

def method(text, percent = 70):
    for i in range(2,len(text)):
        possible = td.decrypt(text,i)
        poss_percent = isEnglish.method(possible)
        if poss_percent > percent:
            print "possible solution: "
            print possible
            print "key: " , i
            print "do you want to keep going? (y/n): "
            answer = raw_input(">>>")
            if answer == "n":
                break



if __name__ =="__main__":
    main()     

