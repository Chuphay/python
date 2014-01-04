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

            
