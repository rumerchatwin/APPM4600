# import libraries
import numpy as np

def question1():
  a = 2
  b = 4.5
  tol = 10E-10
  nmax = 100
  f = lambda x: np.exp(x**2 + 7*x -30) - 1

  [xstar, ier] = bisection(f, a,b,tol,nmax)
  print('The root from bisection method is', )
  print('The error given is', ier)


def bisection(f,a,b,tol,Nmax):
    '''     first verify there is a root we can find in the interval '''
    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

    ''' verify end point is not a root '''
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)

      if (fc ==0):
        astar = c
        ier = 0
        return [astar, ier]

      if (fa*fc<0):
         b = c
      elif (fb*fc<0):
        a = c
        fa = fc
      else:
        astar = c
        ier = 3
        return [astar, ier]

      if (abs(b-a)<tol):
        astar = a
        ier =0
        return [astar, ier]
      
      count = count +1

    astar = a
    ier = 2
    return [astar,ier]


# define routines
def newton(f, fp, fp2, p0,tol,Nmax):
  p = np.zeros(Nmax+1)
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0) / fp(p0)
      p[it+1] = p1
      g = ( f(p1)*fp2(p1) ) / (fp(p1))**2
      if (g > 1):
          info = 1
          pstar = p1
          return[pstar, info, it]
      else:
        if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1

  pstar = p1
  info = 1
  return [p,pstar,info,it]

        
def bisection_Newton(f,fp,fp2,a,b,tol,Nmax):
    #Error codes
    fa = f(a)
    fb = f(b)
    if (fa*fb > 0):
       ier = 1
       astar = a
    elif (fa == 0):
      astar = a
      ier =0
    elif (fb == 0):
      astar = b
      ier = 0
  
    if (ier == 1):
      pstar = astar
      count = 0
      return[pstar, ier, count]
    
    else:
      #begin bisection method
      count = 0
      while (count < Nmax):
        c = 0.5*(a+b)
        fc = f(c)

        if (fc ==0):
          astar = c
          ier = 0

        if (fa*fc<0):
          b = c

        elif (fb*fc<0):
          a = c
          fa = fc

        else:
          astar = c
          ier = 3

        if (abs(b-a)<tol):
          astar = a
          ier =0
        count = count +1
      
      # if the error is not zero, it did not work, so return 
      if (ier != 0):
        pstar = astar
        return[pstar, ier, count]
      
      #begin the newton method
      else:
        midpoint = astar
        g = ( f(midpoint)*fp2(midpoint) ) / (fp(midpoint))**2

        if (g > 1):
          ier = 1
          pstar = midpoint
          return[pstar,ier,count]
        
        else:
          p = np.zeros(Nmax+1)
          p[0] = midpoint
          count = 0
          for count in range(Nmax):
              p1 = midpoint - f(midpoint) / fp(midpoint)
              p[count+1] = p1
              if (abs(p1-p0) < tol):
                pstar = p1
                ier = 0
                return [pstar,ier,count]
              p0 = p1

          pstar = p1
          ier = 1
          return [pstar,ier,count]

question1()




