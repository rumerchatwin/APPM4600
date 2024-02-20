# import libraries
import numpy as np
        
# define routines
def newton(f, fp, fp2, p0,tol,Nmax):
  p = np.zeros(Nmax+1)
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0) / fp(p0)
      p[it+1] = p1
      if (fp(p1) > 1):
          ier = 1
          pstar = p1
          return[pstar, ier, it]
      else:
        if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1

  pstar = p1
  info = 1
  return [p,pstar,info,it]
        

