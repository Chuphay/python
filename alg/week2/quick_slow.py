import random

def quicksort(l):
    if len(l) <= 1:
        return l
    else:    
        rdm = random.randint(0,len(l)-1)
        l[0],l[rdm] = l[rdm],l[0]
        i=1
        for j in range(1,len(l)):
            if l[0]>l[j]:
                l[i],l[j] = l[j],l[i]
                i+=1
        l[0],l[i-1] = l[i-1],l[0] 
        return quicksort(l[:i])+quicksort(l[i:])
