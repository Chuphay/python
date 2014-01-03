# first order approximation of a particle under the influence of gravity
from Tkinter import *
master = Tk()
w = Canvas(master, width = 500, height =500)
w.pack()
def get_position(old_position,velocity,time):
    return [old_position[0] + velocity[0]*time,old_position[1] + velocity[1]*time]
def get_velocity(old_velocity,acceleration,time):
    return [old_velocity[0] + acceleration[0]*time,old_velocity[1] + acceleration[1]*time]
p= [120.,0.]
v = [0.,0.6]
step = 0.5
for i in range(2000):
    print (i)*step, p
    old_p = p
    old_v = v
    dist = (p[0]**2 + p[1]**2)**0.5
    acc = [-70*p[0]/(dist**3),-70*p[1]/(dist**3)]
    p = get_position(old_p,old_v,step)
    v = get_velocity(old_v,acc,step)
    w.create_line (old_p[0]+250,old_p[1]+250,p[0]+250,p[1]+250)
    
    

            

            
            

