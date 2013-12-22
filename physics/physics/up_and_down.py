x_in = [0.0,0.5,1.0,1.5,2.0]
dat = [1.0,0.938470,0.765198,0.511828,0.223891]
memo = {}
def aitken(place,x,points,data):
    if place[0] == 0:
        memo[place] = data[place[1]]
    if not place in memo:
        i = place[1]
        j = place[0]+place[1]   
        A = aitken((place[0]-1,place[1]),x,points,data)
        B = aitken((place[0]-1,place[1]+1),x,points,data)
        memo[place] = A*(x-points[j])/(points[i]-points[j])+B*(x-points[i])/(points[j]-points[i])  
    return memo[place]
print aitken((4,0),0.9,x_in,dat)        
print memo  


         
   
