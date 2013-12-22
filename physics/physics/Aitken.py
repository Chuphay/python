def method(x,points,data):
    """Points should come in like [0.0, 0.5, 1.0, 1.5],
       in which case data will be [f(0), f(0.5), f(1), f(1.5)],
       and finally x is the value that gives f(x), 
       which is what will be returned to you"""
    if len(data) == 1:
        return data[0]
    else:
        A = method(x,points[1:],data[1:])*(x - points[0])/(points[-1] - points[0])
        B = method(x,points[:-1],data[:-1])*(x - points[-1])/(points[0] - points[-1])
        return A+B
