"""making a vigenere encrypter and decrypter in this module"""

alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, key):
    text = text.lower()
    out = []
    n = 0
    for i, letter in enumerate(text):
        try:
            j = key[n%len(key)]
            k = (alpha.index(letter)+alpha.index(j))%len(alpha)
            out.append(alpha[k])
            n += 1
        except ValueError:
            out.append(letter)            
    out = "".join(out)
    return out

def decrypt(text, key):
    text = text.lower()
    out = []
    n = 0
    for i, letter in enumerate(text):
        try:
            j = key[n%len(key)]
            k = (alpha.index(letter)-alpha.index(j))%len(alpha)
            out.append(alpha[k])
            n += 1
        except ValueError:
            out.append(letter)            
    out = "".join(out)
    return out



def main():
    jedi = open("/home/chuphay/python/projects/codes/text/jedi.txt").read()
    s = "use the force luke"
    t = "qsv mos lkrtx siqa"
    key = "warthog"
    #print ciph
    #print
    zee = encrypt(jedi, key) 
    print encrypt(s, key)
    print decrypt(zee, key)


if __name__ == "__main__":
    main()    
