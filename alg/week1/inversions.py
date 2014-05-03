def method(l):
    global i
    i = 0
    def merge_sort(l):
        n = len(l)
        if n>1:
            A, B = merge_sort(l[:n/2]), merge_sort(l[n/2:])
            l = []
            try:
                for k in xrange(n):
                    if A[0]<B[0]:
                        l.append(A.pop(0))
                    else:
                        global i
                        i += len(A)
                        l.append(B.pop(0))
            except IndexError:
                l += A + B
        return l 
    merge_sort(l)
    return i  

def invert_this(l,places):
    """invert two numbers in a list
    if you input [1,2,3,4], [0]
    then the list will be [2,1,3,4] modified in place
    similarily, if  l = [1,2,3,4], places = [1,2]
    then the list will be [1,3,4,2]
    """
    for i in range(len(places)):
        l[places[i]],l[places[i]+1] = l[places[i]+1], l[places[i]]
    return None
    
if __name__ == "__main__":
    from random import shuffle
    l = [1,2,3,4]
    invert_this(l,[2])
    print l
    l = [1,2,3,4]
    invert_this(l,[1,2])
    print l
    l = [i for i in xrange(1000)]
    a = [i for i in xrange(998)]
    shuffle(a)
    a = a[:100]
    invert_this(l,a)
    print method(l)
  
	
