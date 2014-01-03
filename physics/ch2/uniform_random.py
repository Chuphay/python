from datetime import datetime
now = datetime.now()
seed = now.year + 70*(now.month + 12*(now.day + 31*(now.hour + 23*(now.minute +59*now.second))))

def ranf(*args):
    """We are claiming a global variable called seed in this module.
    seed is a number based on some algorithm that has to do with the time
    you can either use the seed provided, or provide your own.
    if you need access to the seed variable, try
    import uniform_random as rdm
    print rdm.seed    
    """
    if len(args) == 0:
        global seed
        x = seed
    else:
        x = args[0]
    a, c, q, r = 16807, 2147483647, 127773, 2836 
    h, l = x/q, x%q
    t = a*l - r*h
    if t>0:
        seed = t
        return float(t)/c
    else:
        seed = c+t            
        return float(c+t)/c   

  
    
            
