import gauss_elim as m
class Spline(object):
    """A class"""
    def __init__(self,x,f):
        self.x = x
        self.f = f
    def stuff(self):
        A = [[0 for i in range(len(self.x)-2)] for j in range(len(self.x)-2)]
        B = [0 for i in range(len(self.x)-2)]
        for i in range(len(self.x)-2):
            for j in range(len(self.x)-2):
                if i == j:
                    A[i][j] = 2*(self.x[i+2]-self.x[i])
                elif i == j-1:
                    A[i][j] = self.x[i+1] - self.x[i]
                elif i == j+1:
                    A[i][j] = self.x[i] - self.x[i-1]       
            B[i] = 6*(self.f[i+2] - 2*self.f[i+1] + self.f[i])
        return (A,B)               
    def get(self):
        out =  m.method(self.stuff()[0],self.stuff()[1])   
        out.insert(0,0.0)
        out.append(0.0)
        return out
    def get_out(self):
        out = [0]*(len(self.x)-1)
        p = self.get()
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
lemon = Spline([-1.0,0.0,1.0,2.0],[2.0,1.0,2.0,5.0])
apple = Spline([-1.0,0.0,1.0],[1.0,2.0,-1.0])
orange = Spline([-2.0,-1.0,0.0,1.0,2.0],[5.0,2.0,1.0,2.0,5.0])
print apple.get_out()
print lemon.get_out() 
print orange.get_out()       
