#we are doing the classic value of pi by throwing darts at one quadrant
from uniform_random import ranf

count = 0
amount = 100000
for i in range(amount):
    x = ranf()
    y = ranf() 
    r_sq = x*x + y*y
    if r_sq <= 1:
        count +=1
print 4*float(count)/amount     

