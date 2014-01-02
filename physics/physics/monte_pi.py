#we are doing the classic value of pi by throwing darts at one quadrant
from uniform_random import ranf
count = 0
seed = 2147483647*ranf()
amount = 1000000
for i in range(amount):
    x = ranf(seed)
    seed = int(x*2147483647-1)
    y = ranf(seed) 
    seed = int(y*2147483647-5)
    r_sq = x*x + y*y
    if r_sq <= 1:
        count +=1
print 4*float(count)/amount     

