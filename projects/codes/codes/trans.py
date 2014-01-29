def badEncrypt(text,key):
    temp = text[:]
    output = ""
    rows = len(text)/key 
    if len(text)%key != 0:
        rows += 1
    null = " "*key
    temp = temp 
    matrix = [["" for i in range(key)] for j in range(rows)]
    for i in range(rows):
        for j in range(key):
            try:
                matrix[i][j] = temp[0]
                temp =  temp[1:] 
            except IndexError:
                pass    
    for i in range(key):
        for j in range(rows):
            output += matrix[j][i]          
    return output 
def encryptMessage(message, key): 
    # from http://inventwithpython.com/hackingciphers.pdf 
    ciphertext = ['']*key 
    for col in range(key): 
        pointer = col  
        while pointer < len(message): 
            ciphertext[col] += message[pointer] 
            pointer += key 
    return ''.join(ciphertext)
def encrypt(text,key):
    output = ""
    for i in range(key):
        for j in range(len(text)):
            if (j+i)%(key) == i:
                try:
                    output += text[j+i]
                except IndexError:
                    pass    
    return output       
def main():
    text = """Space... the Final Frontier. These are the voyages of the starship Enterprise. Its continuing mission: to explore strange new worlds, to seek out new life and new civilizations, to boldly go where no one has gone before."""
    key = 3
    print badEncrypt(text,key)  + "|"  
    print encryptMessage(text,key)  + "|" 
    print encrypt(text,key) + "|" 
if __name__ == '__main__': 
    main() 
      
