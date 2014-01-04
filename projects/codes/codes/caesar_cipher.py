alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
'o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(s,key):
    s = s.replace("\n", "")
    s = s.lower()
    output = ""
    for i in s:
        try:
            j = (alphabet.index(i)+key)%len(alphabet)
            output += alphabet[j]
        except ValueError:
            output += i    
    return output
       
