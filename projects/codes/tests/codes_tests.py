from nose.tools import *
import mock
from sys import stdout
from test.test_support import captured_stdout
import codes.caesar_cipher as csr
import codes.frequency as f
import codes.crack as crack


z = 'ESTD TD DZXP PILXAWP EPIE EZ OZ L NTASPC ZY'
y = 'this is some example text to do a cipher on'
words = open("text/test.txt").read()

def test_caesar():
    
    x = csr.encrypt(words,11)
    assert_equal(x,z)
    assert_equal(csr.encrypt(z,-11),y)

def test_frequency():
    clueless = open("/home/chuphay/python/projects/codes/text/clueless.txt", "r").read()
    obama = open("/home/chuphay/python/projects/codes/text/obama.txt", "r").read()
    z =  f.get_letter(clueless)
    y =  f.get_word(clueless) 
    a = f.get_letter(obama)
    b = f.get_word(obama)
    c = dict( (n, z.get(n, 0)+a.get(n, 0)) for n in set(z)|set(a) )
    d = dict( (n, y.get(n, 0)+b.get(n, 0)) for n in set(y)|set(b) )
    assert_equal(f.get_top(c,3),[(' ', 3455), ('e', 2007), ('t', 1436)])
    assert_equal(f.get_top(d,3),[('the', 173), ('and', 127), ('of', 96)])
    
def test_crack():
     with mock.patch('__builtin__.raw_input', return_value='help'):
         assert crack.response() == 'So sorry. Help system has not been implemented.'

    #assert v == z #'So sorry. Help system has not been implemented.'
   
    
    
