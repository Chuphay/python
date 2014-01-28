import inversions, frequency
import caesar_cipher as caesar

alpha = "abcdefghijklmnopqrstuvwxyz"

english = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

def countInversions(l):
    """so we have to count inversions against the standard etaoin...
    so, if it comes in as etaoin... it should return 0
    but teaoin... should return 1.
    so first, we will have to convert etaoin into numbers. 
    I guess for this list, we just assume that the list is in English
    """
    numbers = [english.index(letter) for letter in l]
    return inversions.method(numbers)

def prepare(text):
    """this will take a text as input, and put the letters in order of most frequent 
    """
    text = text.lower()
    text = [i for i in text if i in alpha]
    text = "".join(text)
    out = [i[0] for i in frequency.top(frequency.letters(text))]
    return out

def method(text):
    """here's the main method for this module.
    it'll take some text, clean it up, see how far away it is from regular english
    and print the text that is closest to english, and return the key
    """
    letters = prepare(text)
    key = []
    for i in range(26):
        attempt = []
        for letter in letters:
            j = (alpha.index(letter)+i)%len(alpha)
            attempt.append(alpha[j])
        key.append((countInversions(attempt),i))
    output = (325,26)
    for i in key:
        if i[0]<output[0]:
            output = (i[0],i[1])
    print caesar.encrypt(text,output[1])  
    return output[1]       
                    

def main():
    jedi = open("/home/chuphay/python/projects/codes/text/jedi.txt").read()
    #print jedi
    zee = prepare(jedi)
    ciph = caesar.encrypt(jedi,1)
    ciff = prepare(ciph)
    #print ciph
    #print countInversions(zee)
    #print countInversions(ciff)
    print method(ciph)
    print 13*25

if __name__ == "__main__":
    main()        
