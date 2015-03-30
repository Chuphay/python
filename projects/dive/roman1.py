"""Taking this from dive into python"""
import sys

class OutOfRangeError(ValueError):
    pass  

class NotIntegerError(ValueError): pass

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))               

def to_roman(n):
    '''convert integer to Roman numeral'''
    result = ''
    if not isinstance(n, int): raise NotIntegerError('integers!')
    if(n>= 4000):
        raise OutOfRangeError('number too big, must be below 4000')
    if(n<=0):
        raise OutOfRangeError('number too small, must be above zero')
    for numeral, integer in roman_numeral_map:
        while n >= integer:                    
            result += numeral
            n -= integer
    return result


print(sys.argv[1])
