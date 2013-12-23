x_in = [0.0,0.5,1.0,1.5,2.0]
dat = [1.0,0.938470,0.765198,0.511828,0.223891]
memo = {}
def aitken(x,points,data,place):
    if place[0] == 0:
        memo[place] = data[place[1]]
    if not place in memo:
        i = place[1]
        j = place[0]+place[1]   
        A = aitken(x,points,data,(place[0]-1,place[1]))
        B = aitken(x,points,data,(place[0]-1,place[1]+1))
        memo[place] = A*(x-points[j])/(points[i]-points[j])+B*(x-points[i])/(points[j]-points[i])  
    return memo[place]
print aitken(0.9,x_in,dat,(4,0))        
#print memo  
def find_closest(x,points):
    check = x - points[0]
    out = 0.0
    for m,n in enumerate(points):
        if abs(x-n)<=check:
            out = m
            check = abs(x-n)
    return out
#print find_closest(0.9,x_in)
memoUp = {} 
memoDown = {}
def up(x,points,data,place):
    if place[0] == 0:
        memoUp[place] = data[place[1]]
    if not place in memoUp:
        i = place[0]
        j = place[1]
        A = up(x,points,data,(i-1,j))
        B = down(x,points,data,(i-1,j+1))
        memoUp[place] = (A-B)*(points[i+j]-x)/(points[i+j]-points[j]) 
    return memoUp[place]     
def down(x,points,data,place):
    if place[0] == 0:
        memoDown[place] = data[place[1]]
    if not place in memoDown:
        
        i = place[0]
        j = place[1]
        A = up(x,points,data,(i-1,j))
        B = down(x,points,data,(i-1,j+1))
        memoDown[place] = (A-B)*(points[j]-x)/(points[i+j]-points[j]) 
    return memoDown[place]           
       
#print up(0.9,x_in,dat,(0,1))  
#print memoUp 
#print memoDown 
def method(x,points,data,order):
    closest = find_closest(x,points)
    k = closest
    j = closest 
    n = len(data)-1
    f = data[closest]
    dx = x - points[closest]
    for y in range(1,order+1):
        if (dx<0 or k == n) and j != 0:
            dx = -dx
            f += down(x,points,data,(y,j))
            j -= 1
        else:
            dx = -dx
            f += up(x,points,data,(y,j))
            k += 1  
    return f       
        
print method(0.9,x_in,dat,4)                
        

         
   
