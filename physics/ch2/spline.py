import gauss_elim as m
class Spline(object):
    """A class...
    dont really know how to use these for regular purposes
    but I guess because there are a lot of methods
    it makes sense
    """
    def __init__(self,x,f):
        """ initilize and stuff...
        same as always
        x should be a list of the inputs:
        [-1.0,0.0,1.0]
        then f should be the data at those points:
        [f(-1),f(0),f(1)]
        """
        l = len(x)
        # here we set up some matrix to solve for p double prime
        A = [[0 for i in range(l-2)] for j in range(l-2)]
        B = [0 for i in range(l-2)]
        for i in range(l-2):
            for j in range(l-2):
                if i == j:
                    A[i][j] = 2*(x[i+2]-x[i])
                elif i == j-1:
                    A[i][j] = x[i+1] - x[i]
                elif i == j+1:
                    A[i][j] = x[i] - x[i-1]       
            B[i] = 6*(f[i+2] - 2*f[i+1] + f[i])
        # here we actually solve for p double prime             
        p =  m.method(A,B)   
        p.insert(0,0.0)
        p.append(0.0)
        # here
        self.x = x
        self.f = f
        self.p = p
        
    def get_out(self):
        """ here we get the coefficients for the spline
        for example, you may get 
        [[-1.0, -3.0, -1.0, 2.0], [1.0, -3.0, -1.0, 2.0]]
        you should interpret this as
        p_0 = -x**3 - 3*x**2 -x + 2
        p_1 = x**3 - 3*x**2 -x + 2
        """
        out = [0]*(len(self.x)-1)
        p = self.p
        x = self.x
        f = self.f
        for i in range(len(x)-1):
            h = x[i+1]-x[i]
            a = p[i+1]/(6.0*h) 
            b = -p[i]/(6.0*h)
            c = f[i+1]/h - h*p[i+1]/6.0
            d = -f[i]/h + h*p[i]/6.0
            o = round(a+b,6)
            m = round(-3*(a*x[i]+b*x[i+1]),6)
            n = round(3*a*x[i]*x[i]+3*b*x[i+1]*x[i+1]+c+d,6)
            q = round(-a*x[i]*x[i]*x[i]-b*x[i+1]*x[i+1]*x[i+1]-c*x[i]-d*x[i+1],6)
            out[i]=[o,m,n,q]
        return out
    def get_x(self,target):
        pass
    def draw(self):
        pass                     


lemon = Spline([-1.0,0.0,1.0,2.0],[2.0,1.0,2.0,5.0])
apple = Spline([-1.0,0.0,1.0],[1.0,2.0,-1.0])
orange = Spline([-2.0,-1.0,0.0,1.0,2.0],[5.0,2.0,1.0,2.0,5.0])
print apple.get_out()
print lemon.get_out() 
print orange.get_out()       
