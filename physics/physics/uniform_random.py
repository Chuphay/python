from datetime import datetime

def ranf(*args):
    """Either pass a seed to this, or it will generate a seed for you.
    to get a new seed, try 
    x = ranf(old_seed)
    new_seed = int(x*2147483647) 
    please do not repeatedly call ranf() within the same second
    it will give you the same number repeatedly    
    """
    if len(args) == 0:
        now = datetime.now()
        x = now.year + 70*(now.month + 12*(now.day + 31*(now.hour + 23*(now.minute +59*now.second))))
    else:
        x = args[0]
    a, c, q, r = 16807, 2147483647, 127773, 2836 
    h, l = x/q, x%q
    t = a*l - r*h
    if t>0:
        return float(t)/c
    else:           
        return float(c+t)/c   

   
    
            
