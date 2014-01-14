def badDecrypt(text,key):
    out = []
    cols = len(text)/key
    if len(text)%key !=0:
        cols +=1  
    matrix = [[0 for i in range(cols)] for j in range(key)]
    empty = cols*key - len(text)
    for i in range(empty):
        matrix[key-1-i][cols-1] = "#"
    for i in range(key):
        for j in range(cols):
            if matrix[i][j] == "#":
                continue
            else:
                matrix[i][j] = text[0]
                text = text[1:]
    for i in range(cols):
        for j in range(key):
            if matrix[j][i] != "#":
                out.append(matrix[j][i])            
    return "".join(out)                
                
def decryptMessage(message, key):
    #from http://inventwithpython.com/hackingciphers.pdf 
    numOfColumns = len(message)/key
    if len(message)%key != 0:
        numOfColumns +=1   
    numOfRows = key  
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = ['']*numOfColumns 
    col = 0 
    row = 0 
    for symbol in message: 
        plaintext[col] += symbol 
        col += 1 
        # If there are no more columns OR we're at a shaded box, go back to 
        # the first column and the next row. 
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= 
numOfRows - numOfShadedBoxes): 
            col = 0 
            row += 1 
    return ''.join(plaintext)

def decrypt(text, key):
    """note, we use the # symbol internally,
so if the cipher has hash symbols, please use a differnt decryption scheme"""
    output = ""
    cols = len(text)/key
    if len(text)%key != 0 :
        cols += 1
    l = len(text)
    for i in range(cols*key - l):
        text = text[:l-i*(cols-1)] + "#" +text[l-i*(cols-1):]      
    for i in range(cols):
        for j in range(len(text)):
            if (j+i)%(cols) == i:
                output += text[j+i]
    return output.replace("#", "")
 
         
def main():    
    text ="apples and oranges are good for you, isn't that very true?"
    key = 23
    print badDecrypt(text,key)
    print decrypt(text,key)
    print decryptMessage(text,key)    
if __name__ == "__main__":
    main()    
