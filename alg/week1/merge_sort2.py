def merge_sort(l):
    n = len(l)
    if n>1:
        A, B = merge_sort(l[:n/2]), merge_sort(l[n/2:])
        l = []
        i, j = 0,0
        try:
            
            for k in xrange(n):
                if A[i]<B[j]:
                    l.append(A[i])
                    i += 1
                else:
                    l.append(B[j])
                    j += 1
        except IndexError:
            l += A[i:] + B[j:]
    return l            
  
