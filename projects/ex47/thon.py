S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 1]
def output(s):
    return [[x,x.upper(),len(x)] for x in s.split(' ')]
#out = output("hello world yo 3")
#print out
def factor(x):
    return [i for i in range(1,x + 1) if x%i == 0]
  
#print factor(99876)    
def func(*args):
    output = 1
    print len(args),args
    if len(args)==1:
        if len(args[0])== 1:
            return args[0][0]   
    else:
 
        for n in range(len(args)):
            print func(args[n])
            output *= 3 #func(args[n])
        return output
print func([1,[2,3]],[4,5])    
    

