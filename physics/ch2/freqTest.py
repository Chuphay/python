import myRandom as rdm
import Tkinter
master = Tkinter.Tk()



def draw(points):
    w = Tkinter.Canvas(master, width=500, height=200)
    w.pack()
    v = 500.0/len(points)
    z = [0 for i in range(60)]
    for i in range(60):
        j = i - 30
        for x in points:
            if x>j/10.0 and x<(j+1)/10.0:
                z[i] +=1
        j = j+30        
        w.create_line(j*2,-z[i-1]*v+100,(j+1)*2,-z[i]*v+100)            


x = [rdm.ranf() for i in range(1000)]
y = [rdm.rane() for i in range(10000)]
z = [rdm.rang() for i in range(10000)]
draw(x)
draw(y)
draw(z)        

Tkinter.mainloop()
