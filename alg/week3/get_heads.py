import random
import numpy as np

def flip_coin():
    flip = np.random.randn()
    #print flip
    if flip>0:
        return 1
    else:
        return 0

def play():
    i = 1
    #print True == flip_coin() 
    while flip_coin()==False:
        i +=1
    return i    

data = []
for i in range(100):

    data.append(play())
                   
data = np.array(data)
print data
print data.mean()
    
