import random


def comparisons(l):
    global out
    out = 0
    def quicksort(l):
        if len(l) <= 1:
            return l
        else:    
            #rdm = random.randint(0,len(l)-1)

            if len(l)%2 == 0:
                mid = (l[len(l)/2-1],len(l)/2-1)
            else:
                mid = (l[len(l)/2],len(l)/2)
            start,end = l[0], l[len(l)-1] 
            if (mid[0]>=start and mid[0]<=end) or (mid[0]<=start and mid[0]>=end):
                do = mid
            elif (start>=mid[0] and start<=end) or(start<=mid[0] and start>=end):
                do = (start,0)
            elif (end>=mid[0] and end<=start) or(end<=mid[0] and end>=start): 
                do = (end,len(l)-1)
            else:
                raise IndexError 
            
            rdm = random.randint(0,len(l)-1)                      
            l[0],l[rdm] = l[rdm],l[0]
            a = l[0]
            i=1
            for j in range(1,len(l)):
                global out 
                out += 1
                if a>l[j]:
                    l[i],l[j] = l[j],l[i]
                    i+=1
            l[0],l[i-1] = l[i-1],l[0] 
            return quicksort(l[:i-1])+[a]+quicksort(l[i:])
    quicksort(l)
    return out
      
if __name__ == '__main__':
    l = [1,2,3,4,0,-1,2,6,7]
    print l
    print comparisons(l)
    
