def method(m,points,data):
    n = len(data)-1
    u,s,g,h = [],[],[],[]
    if m>n:
        m = n
        print "The highest power is adjusted to: " + str(n)
    for i in range(m+1):
        u.append([None]*(n+2))
        u[i][n+1] = 0
        s.append(0) 
        g.append(0) 
        h.append(0)    
    for i in range(n+1):
        u[0][i] = 1
        stmp = u[0][i]**2
        s[0] += stmp
        g[0] += points[i]*stmp
        u[0][n+1] += u[0][i]*data[i]
    g[0] = g[0]/s[0]
    u[0][n+1] = u[0][n+1]/s[0]
    for i in range(n+1): 
        u[1][i] = points[i]*u[0][i]-g[0]*u[0][i]
        s[1] += u[1][i]**2
        g[1] += points[i]*u[1][i]**2
        h[1] += points[i]*u[1][i]*u[0][i]
        u[1][n+1] += u[1][i]*data[i]
    g[1] = g[1]/s[1]
    h[1] = h[1]/s[0]
    u[1][n+1] = u[1][n+1]/s[1]  
    if m>=2:
        for i in range(1,m):
            for j in range(n+1):
                u[i+1][j] = points[j]*u[i][j]-g[i]*u[i][j]-h[i]*u[i-1][j]
                s[i+1] += u[i+1][j]**2
                g[i+1] += points[j]*u[i+1][j]**2
                h[i+1] += points[j]*u[i+1][j]*u[i][j]
                u[i+1][n+1] += u[i+1][j]*data[j]
            g[i+1] = g[i+1]/s[i+1]
            h[i+1] = h[i+1]/s[i]
            u[i+1][n+1] = u[i+1][n+1]/s[i+1]    
    return u  
           
 
