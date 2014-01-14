from nose.tools import *
import random
import codes.caesar_cipher as csr
import codes.frequency as f
import codes.trans as trans
import codes.transDecrypt as td
import codes.crackMath
import codes.affineCipher 



z = 'ESTD TD DZXP PILXAWP EPIE EZ OZ L NTASPC ZY'
y = 'this is some example text to do a cipher on'
#words = open("text/test.txt").read()

def test_caesar():
    x = csr.encrypt(y,11)
    assert_equal(x,z)
    assert_equal(csr.encrypt(z,-11),y)

def test_frequency():
    clueless = open("/home/chuphay/python/projects/codes/text/clueless.txt", "r").read()
    obama = open("/home/chuphay/python/projects/codes/text/obama.txt", "r").read()
    z =  f.letters(clueless)
    y =  f.words(clueless) 
    a = f.letters(obama)
    b = f.words(obama)
    c = dict( (n, z.get(n, 0)+a.get(n, 0)) for n in set(z)|set(a) )
    d = dict( (n, y.get(n, 0)+b.get(n, 0)) for n in set(y)|set(b) )
    assert_equal(f.top10(c),[('e', 22.17),('t', 15.91),('o', 14.43),('a', 13.87),('s', 11.61),('n', 11.56),('r', 11.07),('i', 10.97),('h', 9.86),('l', 6.89)])
    assert_equal(f.top10(d),[('the', 161.0),('and', 118.0),('of', 96.0),('to', 89.0),('a', 72.0),('our', 59.0),('that', 56.0),('we', 51.0),('is', 48.0),('I', 33.0)])

def test_trans():
    random.seed(42) # set the random "seed" to a static value 
    for i in range(20): 
        # The message will have a random length: 
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 10) 
        # Convert the message string to a list to shuffle it. 
        message = list(message) 
        random.shuffle(message)
        message = ''.join(message) 
        for key in range(1,len(message)):
            #c = trans.badEncrypt(message,key)
            #v = trans.encryptMessage(message,key)
            en = trans.encrypt(message, key)
            #assert_equal(v,c) 
            #assert_equal(v,en)
            #decrypted = td.decryptMessage(en, key)
            de = td.decrypt(en, key)
            #dee = td.badDecrypt(en, key)
            assert_equal(de,message)
          
def test_affine():
    random.seed(42)
    for i in range(20):  
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 10) 
        message = list(message) 
        random.shuffle(message)
        message = ''.join(message)
        key = 0
        while True: 
            key = random.randint(2, 1024) 
            if codes.crackMath.gcd(key, 26) == 1:
                break
        key_B =  random.randint(2, 1024)
        encrypt = codes.affineCipher.encrypt(message,key,key_B)
        decrypt = codes.affineCipher.decrypt(encrypt, key, key_B)
        assert_equal(message.lower(), decrypt)        

           

   
    
    
