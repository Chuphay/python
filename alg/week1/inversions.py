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

    
if __name__ == "__main__":
    num=[1,3,5,2,4,6]
    num2 = [7,6,5,4,3,2,1]
    print method(num)
    print method(num2)   
	
