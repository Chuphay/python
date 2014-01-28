def letters(s):
    s = s.replace("\n" , "")
    s = s.replace(" ","")
    dict = {}
    for i in s:
        try:
            dict[i] += 100.0/len(s)
        except KeyError:
            dict[i]  = 100.0/len(s)        
    return dict 

def words(s):
    s = s.replace("\n" , "")
    s = s.split(" ")
    dict = {}
    for i in s:
        try:
            dict[i] += 1
        except KeyError:
            dict[i]  = 1
    return dict 

def top10(dictionary):
    output = []
    dict = dictionary.copy()
    for i in range(10):
        temp = ("",0)
        for key in dict:
            if dict[key]>temp[1]:
                temp = (key,round(dict[key],2))           
        output.append(temp)
        del dict[temp[0]]
    return output

def top(dictionary):
    output = []
    dict = dictionary.copy()
    
    for i in range(len(dict)):
        temp = ("",0)
        for key in dict:
            if dict[key]>temp[1]:
                temp = (key,round(dict[key],2))           
        output.append(temp)
        del dict[temp[0]]
    return output

def get_string(s,length):
    s = s.replace("\n" , "")
    s = s.replace(" ","")
    s = s.lower()
    dict = {}
    for i in range(len(s)-length):
        string = ""
        for j in range(length):
            string += s[i+j]
        try:
            dict[string] += 1
        except KeyError:
            dict[string]  = 1
    return dict  

library = {}
library['letters'] = [('e', 11.58), ('t', 8.22), ('o', 7.36), ('a', 7.12), ('n', 6.16), ('s', 6.09), ('r', 5.9), ('i', 5.62), ('h', 4.95), ('d', 3.59)]

def main():
    a = """The oldest means of sending secret messages is to simply conceal them by one trick or another. The ancient Greek historian Herodotus wrote that when the Persian Emperor Xerxes moved to attack Greece in 480 BCE, the Greeks were warned by an Greek named Demaratus who was living in exile in Persia. In those days, wooden tablets covered with wax were used for writing. Demaratus wrote a message on the wooden tablet itself and then covered it with wax, allowing the vital information to be smuggled out of the country.

The science of sending concealed messages is known as "steganography", Greek for "concealed writing". Other classical techniques for smuggling a message included tattooing it on the scalp of a messenger, letting his hair grow back, and then sending him on a journey. At the other end, the recipient shaved the messenger's hair off and read the message."""

    #b = open("/home/chuphay/python/projects/codes/text/obama.txt").read()
    #c = open("/home/chuphay/python/projects/codes/text/clueless.txt", "r").read()
    text = a    
    zee = letters(text)
    print top10(zee)
    print library['letters']

if __name__ == "__main__":
    main()    

             
