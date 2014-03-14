def myF(l):
    L =len(l)
    if L == 1:
        return l
    elif L%2 == 0:
        out = [0 for i in range(L)]
        
        for i in range(L/2):
            A = myF(l[::2])
            B = myF(l[1::2])
            out[i] = (A[i] + B[i]*exp(-2j*pi*i/L))
            out[i+L/2] = (A[i] - B[i]*exp(-2j*pi*i/L))
        return out
    else:
        raise ValueError("has to be 2 to the power of something")
