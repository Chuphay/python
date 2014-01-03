def method(x,points,data):
    """This is the standard Aitken method from Tao Pang's computational physics.
       Points should come in like [0.0, 0.5, 1.0, 1.5],
       in which case data will be [f(0), f(0.5), f(1), f(1.5)],
       and finally x is the value that gives f(x), 
       which is what will be returned to you"""
    memo = {}
    place = (len(data)-1,0)
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
    return aitken(x,points,data,place)    
        
def upNdown(x,points,data): 
    """This is the up and down method from Tao Pang's computational physics.
       It's a little more convoluted than the straight forward method,
       but may be better when you have many many data points close together. 
       Points should come in like [0.0, 0.5, 1.0, 1.5],
       in which case data will be [f(0), f(0.5), f(1), f(1.5)],
       and finally x is the value that gives f(x), 
       which is what will be returned to you"""
    memoUp = {} 
    memoDown = {}
    def up(x,points,data,place):
        if place[0] == 0:
            memoUp[place] = data[place[1]]
        if not place in memoUp:
            i = place[0]
            j = place[1]
            A = up(x,points,data,(i-1,j))-down(x,points,data,(i-1,j+1))
            memoUp[place] = A*(points[i+j]-x)/(points[i+j]-points[j])
        return memoUp[place]
    
    def down(x,points,data,place):
        if place[0] == 0:
            memoDown[place] = data[place[1]]
        if not place in memoDown:
            i = place[0]
            j = place[1]
            A = up(x,points,data,(i-1,j))-down(x,points,data,(i-1,j+1))
            memoDown[place] = A*(points[j]-x)/(points[i+j]-points[j])
        return memoDown[place]    
    
    def find_closest(x,points):
        check = abs(points[-1] - points[0])
        answer = 0
        for m,n in enumerate(points):
            if abs(x-n)<= check:
                check = abs(x-n)
                answer = m
        return answer  
             
    def down_up_method(x,points,data,order):
        j = find_closest(x,points)
        dx = x - points[j]
        f = 0
        n = len(data)-1
        for O in range(order+1):
            if dx>0:
                f += up(x,points,data,(O,j))
                if j == n - O:
                    j -= 1
                else:
                    dx = -dx
            else:
                f += down(x,points,data,(O,j)) 
                if j == 0:
                    continue
                else:    
                    dx = -dx 
                    j -= 1
        return f          
    return down_up_method(x,points,data,len(data)-1)         
          
 
