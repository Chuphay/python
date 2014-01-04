#obviously this is the millikan oil drop experiment
#check out Tao Pang's book for more explanation
import least_square as fls
x_in = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
dat = [6.558,8.206,9.88,11.5,13.14,14.82,16.4,18.04,19.68,21.32,22.96,24.6,26.24,27.88,29.52]
u = fls.method(21,x_in,dat)
n = len(dat)-1
sum = 0
for i in range(len(dat)):   
    sum += x_in[i]
e = u[1][n+1]
dq = u[0][n+1]-u[1][n+1]*sum/(n+1)
print "Fundamental charge: " + str(e)
print "Estimated error: " + str(dq)   
c1,c2,c3,c4 = 0, 0, 0, 0
for i in range(len(dat)):
    c1 += x_in[i]
    c2 += x_in[i]**2
    c3 += dat[i]
    c4 += dat[i]*x_in[i]
g = c1*c1-c2*(n+1)
a0 = (c1*c4-c2*c3)/g
a1 = (c1*c3-c4*(n+1))/g
print "Fundamental charge: " + str(a1)
print "Estimated error: " + str(a0)      
