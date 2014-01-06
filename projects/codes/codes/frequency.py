def get_letter(s):
    s = s.replace("\n" , "")
    s= s.lower()
    dict = {}
    for i in s:
        try:
            dict[i] += 1
        except KeyError:
            dict[i]  = 1
    return dict 

def get_word(s):
    s = s.replace("\n" , "")
    s= s.lower()
    s = s.split(" ")
    dict = {}
    for i in s:
        try:
            dict[i] += 1
        except KeyError:
            dict[i]  = 1
    return dict 

def get_most(dict):
    output = ("",0)
    for key in dict:
        if dict[key]>output[1]:
            output = (key,dict[key])
    return output    

def get_top(dict, number):
    output = []
    for i in range(number):
        z = get_most(dict)           
        output.append(z)
        del dict[z[0]]
    return output

            
text = """The oldest means of sending secret messages is to simply conceal them by one trick or another. The ancient Greek historian Herodotus wrote that when the Persian Emperor Xerxes moved to attack Greece in 480 BCE, the Greeks were warned by an Greek named Demaratus who was living in exile in Persia. In those days, wooden tablets covered with wax were used for writing. Demaratus wrote a message on the wooden tablet itself and then covered it with wax, allowing the vital information to be smuggled out of the country.

The science of sending concealed messages is known as "steganography", Greek for "concealed writing". Other classical techniques for smuggling a message included tattooing it on the scalp of a messenger, letting his hair grow back, and then sending him on a journey. At the other end, the recipient shaved the messenger's hair off and read the message."""

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
zee = get_string(text,3)
print get_top(zee,5)
             
