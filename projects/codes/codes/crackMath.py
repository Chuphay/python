def gcd(a, b): 
    """Euclid's Greatest Common Divisor (GCD) algorithm.
The GCD of two positive integers is the largest integer that divides both of them without leaving a remainder."""
    while a != 0: 
        a, b = b % a, a 
    return b 

def isRelativelyPrime(a,b):
    if gcd(a,b) == 1:
        return True
    else:
        return False 
def findModInverse(a, m):
    # from: http://inventwithpython.com/hackingciphers.pdf
    #Euclid's Extended Algorithm 
    if gcd(a, m) != 1: 
        return None # no mod inverse exists if a & m aren't relatively prime 
    u1, u2, u3 = 1, 0, a 
    v1, v2, v3 = 0, 1, m 
    while v3 != 0: 
        q = u3 // v3 # // is the integer division operator 
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3 
    return u1 % m 
               
    
def main():
    print gcd(30,24)
    print gcd(409119243, 87780243)
    print isRelativelyPrime(27,28)
    print isRelativelyPrime(81,351)
    print findModInverse(7,26)
    
if __name__ == "__main__":
    main()         
    

