import first_least_square as fls
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
