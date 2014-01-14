# Affine Cipher Hacker 
# http://inventwithpython.com/hacking (BSD Licensed) 
 
import pyperclip, affineCipher, isEnglish, crackMath, random 
 
SILENT_MODE = False 
def main(): 
    # You might want to copy & paste this text from the source code at 
    # http://invpy.com/affineHacker.py 
    myMessage = """"U OEKBMPIV GEMNL LISIVJI PE RI OUNNIL WHPINNWCIHP WF WP 
    OEMNL LIOIWJI U ZMKUH WHPE RINWIJWHC PZUP WP GUS ZMKUH." -UNUH PMVWHC""" 
 
    hackedMessage = hackAffine(myMessage) 
 
    if hackedMessage != None: 
        # The plaintext is displayed on the screen. For the convenience of 
        # the user, we copy the text of the code to the clipboard. 
        print('Copying hacked message to clipboard:') 
        print(hackedMessage) 
        pyperclip.copy(hackedMessage) 
    else: 
        print('Failed to hack encryption.') 
 
 
def hackAffine(message): 
    print('Hacking...') 
 
    # Python programs can be stopped at any time by pressing Ctrl-C (on 
    # Windows) or Ctrl-D (on Mac and Linux) 
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)') 
 
    # brute-force by looping through every possible key 
    for i in range(26 ** 2): 
        key = 0
        while True: 
            key = random.randint(2, 1024) 
            if crackMath.gcd(key, 26) == 1:
                break
        for j in range(1,26):
 
            decryptedText = affineCipher.decrypt(message,key,j) 
            if not SILENT_MODE: 
                print 'Tried Key %s, %s... (%s)' % (key, j, decryptedText[:40]) 
 
            if isEnglish.method(decryptedText)>70: 
                # Check with the user if the decrypted key has been found. 
                print 
                print'Possible encryption hack:' 
                print'Key: %s, %s' % (key, j) 
                print'Decrypted message: ' + decryptedText[:200] 
                print
                print'Enter D for done, or just press Enter to continue hacking:' 
                response = raw_input('> ') 
                if response.strip().upper().startswith('D'): 
                    return decryptedText
                else:
                    continue     
    return None 

# If affineHacker.py is run (instead of imported as a module) call 
# the main() function. 
if __name__ == '__main__': 
    main() 

