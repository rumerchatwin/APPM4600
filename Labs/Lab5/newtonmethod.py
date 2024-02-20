# import libraries
import numpy as np

def newtonmethod(p0, f, fp, fp2, tol, nmax):
    count = 0
    while (count < nmax):
        count =+ 1
        p = p0 - f(p0)/fp(p0)
        g = (f(p)*fp2(p))/(fp(p))**2
        if (fp(p) > 1):
            ier = 1
            pstar = p
            return[pstar, ier, count]
        else:
            if (abs(p-p0) < tol):
                pstar = p
                ier = 0
                return[pstar, ier, count]
        p = p0
    
    
        
        




