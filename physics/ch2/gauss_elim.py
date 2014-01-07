def method(matrix,constants):
    """For example:
       matrix =[[2,4,0],[2,1,-1],[0,-2,-1]]
       constant = [2,3,2]
       |2  4  0| | x |   | 2 |
       |2  1 -1| | y | = | 3 |
       |0 -2 -1| | z |   | 2 |
       and [x,y,z] will be returned
       I believe this code will fail if any of the diagonal elements are zero
       in which case, simply manually move them around 
    """
    #here we copy the code, and make sure everything is a float
    m, c = matrix[:] , constants[:]
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = float(m[i][j])
        c[i] = float(c[i])
    #here we do our gaussian elimination
    for i in range(len(m)):
        norm = m[i][i]
        try:
            c[i] = c[i]/norm
        except ZeroDivisionError:
            print """oops... it looks like one of the diagonal elements 
                     became zero. Please try rearranging your matrix."""
            break                 
        for j in range(len(m)):
            m[i][j] = m[i][j]/norm
        for j in range(i+1,len(m)):
            size = m[j][i]
            c[j] = c[j]-size*c[i]
            for k in range(len(m)):
                m[j][k] = m[j][k]-size*m[i][k]
    #here we solve for our output
    output = [0]*len(m)
    for i, e in reversed(list(enumerate(m))):
        out = 0
        for j, n in reversed(list(enumerate(e))):
            if n == 0 or i == j:
                pass
            else:
                out -= n*output[j]    
        out += c.pop()
        output[i] = out
    return output

