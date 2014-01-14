import crackMath

def multiply(text,key):
    out = []
    for i in text:
        if i.isalpha():
            i = i.lower()
            z = ord(i) - 97
            x = chr((z*key)%26+97)
            out.append(x.upper())
        else:
            out.append(i)    
    return "".join(out)

def caesar(text, key):
    out = []
    for i in text:
        if i.isalpha():
            i = i.lower()
            z = ord(i) - 97 + key
            x = chr(z%26+97)
            out.append(x.upper())
        else:
            out.append(i)    
    return "".join(out)

def encrypt(text,key_A, key_B):
    if crackMath.isRelativelyPrime(26,key_A):
        temp = multiply(text,key_A)
        return caesar(temp,key_B)
    else:
        print "could not complete. the length of text and key_A must be relatively prime." 
def decrypt(text,key_A,key_B):
    inverse = crackMath.findModInverse(key_A,26)
    b = caesar(text,-key_B)
    out = []
    for i in b:
        if i.isalpha():
            i = i.lower()
            z = ord(i) - 97
            x = chr((z*inverse)%26+97)
            out.append(x)
        else:
            out.append(i)
    return "".join(out)           
            
                   

def main():        
    print multiply("abcdefghijklmnopqrstuvwxyz",8953851)
    print encrypt("abcdefghijklmnopqrstuvwxyz",8,2)
    myMessage = """"A computer would deserve to be called intelligent if it 
    could deceive a human into believing that it was human." -Alan Turing""" 
    zee = encrypt(myMessage,23,20)
    print zee
    print decrypt(zee,23,20)
    
if __name__ == "__main__":
    main()            
    
