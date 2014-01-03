# motion of a particle in one -d under an elastic force to first order approximation
import Tkinter
master = Tkinter.Tk()
w = Canvas(master, width=500, height=200)
w.pack()
def get_x(old_x,velocity,time):
    return float(old_x + velocity*time)
def get_velocity(old_velocity,acceleration,time):
    return float(old_velocity + acceleration*time)
x = 0
v = 1
step = 1./10
for i in range(200):
    
    print (i)*step, x, v
    x_old = x
    v_old = v
    x = get_x(x_old,v_old,step)
    v = get_velocity(v_old,-x_old,step)
    w.create_line( i*2,x_old*10+100,(i+1)*2,x*10+100)
    w.create_line(i*2,v_old*10+100,(i+1)*2,v*10+100,fill="red", dash=(4, 4))


