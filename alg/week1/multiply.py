"""Integer Multiplication
Input: two n-digit numbers x and y
Output: the product x*y
Primitive Operation - add or multiply 2 single-digit numbers

big note: in python 2.7 01234 == 668
so please don't feed these kinds of numbers into these algorithms
"""
memory = [[0,0,0,0,0,0,0,0,0,0],\
          [0,1,2,3,4,5,6,7,8,9],\
          [0,2,4,6,8,10,12,14,16,18],\
          [0,3,6,9,12,15,18,21,24,27],\
          [0,4,8,12,16,20,24,28,32,36],\
          [0,5,10,15,20,25,30,35,40,45],\
          [0,6,12,18,24,30,36,42,48,54],\
          [0,7,14,21,28,35,42,49,56,63],\
          [0,8,16,24,32,40,48,56,64,72],\
          [0,9,18,27,36,45,54,63,72,81]]
          
def grade_school(x,y):

    #here we turn the inputs into lists
    X = [int(i) for i in str(x)]
    Y = [int(i) for i in str(y)]
    
    #here's the main loop to create the intermediate calculations
    calculations = [[0] for i in xrange(len(Y))] 
    for i,y in enumerate(reversed(Y)):
        add_zeroes = [0 for j in range(i)]
        calculations[i] += add_zeroes
        for j,x in enumerate(reversed(X)):
            from_memory = memory[y][x]+calculations[i][j+i]
            calculations[i][j+i] = (from_memory)%10
            calculations[i].append((from_memory)/10)

    #here we simply add the contributions from the intermediate calculations
    out = 0
    for lst in calculations:
        out += int(''.join(str(i) for i in reversed(lst)))
    return out
    
def karatsuba(x,y):
    """only takes inputs that are of equal length
    and that have length a power of 2
    so 1234*5678 is fine
    but 123*456 is not, nor is 2*12.
    As samos123 pointed out, my program is broken :(
    please check his git repository for a working program:
    https://github.com/samos123/randompythoncode/blob/master/multiplication.py
    or, I have a copy of it in my repo as well
    """
    
    X = [int(i) for i in str(x)]
    Y = [int(i) for i in str(y)] 
    def recurse(X,Y):
        print X,Y
        l_X = len(X)
        l_Y = len(Y)

        if (l_X>1 or l_Y>1):

            a = X[:l_X/2]
            b = X[l_X/2:]
            c = Y[:l_Y/2]
            d = Y[l_Y/2:]

            m = recurse(a,c)
            n = recurse(b,d)
            o_1 = int(''.join(str(i) for i in a))+int(''.join(str(i) for i in b))
            o_2 = int(''.join(str(i) for i in c))+int(''.join(str(i) for i in d))
            o_3 = [int(i) for i in str(o_1)]
            o_4 = [int(i) for i in str(o_2)]
            o = recurse(o_3,o_4)

            return (10**l_X)*m+(10**(l_X/2))*(o-m-n)+n
        else:
            return memory[int(X[0])][int(Y[0])]

    return recurse(X,Y)              

if __name__ == "__main__":

    print karatsuba(21,19) == 21*19


    
                    
    
    
