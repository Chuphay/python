def insert(sorted_list,number):
    """helper function for insert_sort"""
    if len(sorted_list) == 0:
        return [number]
    elif sorted_list[-1] <= number:
        sorted_list.append(number)
        return sorted_list
    else:
        return insert(sorted_list[:-1],number)+sorted_list[-1:]

def insert_sort(unsorted_list):
    """can't sort lists that are over approximately 1000 numbers long
    due to reaching python's recursion limit""" 
    sorted_list = []
    for i in range(len(unsorted_list)):
        sorted_list = insert(sorted_list,unsorted_list[i])
    return sorted_list  
    
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
                    l.append(B.pop(0))
        except IndexError:
            l += A + B
    return l         

if __name__ == '__main__':
    l = [2,1,4,3,7,10,4]
    print merge_sort(l)
    print sorted(l)
    from random import shuffle
    a = [i for i in xrange(100000)]
    shuffle(a)
    b = [i for i in xrange(1000)]
    shuffle(b)
    print a[:10]
    print l
    print insert_sort(b) == sorted(b)
    print merge_sort(a) == sorted(a)
