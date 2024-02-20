# import libraries
import numpy as np

# defining functions for the questions in lab
def question1():
  a = 2
  b = 4.5
  tol = 10E-10
  nmax = 100
  f = lambda x: np.exp(x**2 + 7*x -30) - 1

  [xstar, ier, count] = bisection(f, a,b,tol,nmax)
  print('The root from bisection method is', xstar )
  print('The error given is', ier)
  print('The number of iterations is', count)

def question2():
  a = 2
  b = 4.5
  tol = 10E-10
  nmax = 100
  x0 = 4.5
  f = lambda x: np.exp(x**2 + 7*x -30) - 1
  fp = lambda x: (2*x +7) * np.exp(x**2 + 7*x -30) - 1

  [pstar, ier, count] = newton(f, fp, x0, tol, nmax)
  print('The root from Newton Method is', pstar)
  print('The error is', ier)
  print('The number of iterations is', count)

def question3():
  a = 2
  b = 4.5
  tol = 10E-10
  nmax = 100
  x0 = 4.5
  f = lambda x: np.exp(x**2 + 7*x -30) - 1
  fp = lambda x: (2*x +7) * np.exp(x**2 + 7*x -30) - 1
  fp2 = lambda x: (2 * np.exp(x**2 + 7*x -30) - 1) + (2*x +7)**2 * np.exp(x**2 + 7*x -30) - 1
  [pstar, ier, count] = hybrid(f, fp, fp2, a,b,tol,nmax)
  print('The root for the combined method is', pstar)
  print('The error is', ier)
  print('The number of iterations is', count)

# define the bisection method
def bisection(f,a,b,tol,Nmax):
    '''     first verify there is a root we can find in the interval '''
    fa = f(a)
    fb = f(b)
    count = 0

    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier, count]

    ''' verify end point is not a root '''
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, count]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, count]

    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)

      if (fc ==0):
        astar = c
        ier = 0
        return [astar, ier, count]

      if (fa*fc<0):
         b = c
      elif (fb*fc<0):
        a = c
        fa = fc
      else:
        astar = c
        ier = 3
        return [astar, ier, count]

      if (abs(b-a)<tol):
        astar = a
        ier =0
        return [astar, ier, count]
      
      count = count +1

    astar = a
    ier = 2
    return [astar,ier, count]

#define the hybrid bisection method
def bisection_update(f,fp, fp2,a,b,tol,Nmax):
    fa = f(a)
    fb = f(b)
    count = 0
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier, count]
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, count]
    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, count]

    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)
      #doing the netwon implication first: 
      g = (f(c) * fp2(c)) / (fp(c))**2
      # Now check if g is less than 1
      if (g < 1):
        astar = c
        ier = 0
        return[astar, ier, count]
      else:
        if (fc ==0):
          astar = c
          ier = 0
          return [astar, ier, count]

        if (fa*fc<0):
          b = c
        elif (fb*fc<0):
          a = c
          fa = fc
        else:
          astar = c
          ier = 3
          return [astar, ier, count]

        if (abs(b-a)<tol):
          astar = a
          ier =0
          return [astar, ier, count]
        
        count = count +1

    astar = a
    ier = 2
    return [astar,ier, count]

def newton(f, fp,p0,tol,Nmax):
  p = np.zeros(Nmax+1)
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [pstar,info,it]

        
def hybrid(f,fp,fp2,a,b,tol,Nmax):
    #RETURNS: pstar, ier, count
    #Check for when there will be an error first
    count = 0
    fa = f(a)
    fb = f(b)
    count = 0
    if (fa*fb>0):
       ier = 1
       pstar = a
       return [pstar, ier, count]
    if (fa == 0):
      pstar = a
      ier =0
      return [pstar, ier, count]
    if (fb ==0):
      pstar = b
      ier = 0
      return [pstar, ier, count]
    
    ###############################################
    # Now we have made sure that the bisection method can be started, we want to use the basin of convergence.
    # When the value is in the basin of convergence, we want the bisection method to end. 
    # We set that value equal to the midpoint and then use the Newton method to then find the root for the most accuarcy.
    
    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)
      # checks to see if the first half is the midpoint
      # if this is the case, it is a perfect scenario where it will take zero iterations
      #so Newton method is not involved here
      if (fc == 0):
        pstar = c
        ier = 0
        return[pstar, ier, count]
      # We want to find if the midpoint is in the basin of convergence, so define g
      g = (f(c) * fp2(c)) / (fp(c))**2
      # Now check if g is less than 1
      if (g < 1):
        midpoint = c
        [pstar, ier, newton_portion] = newton(f, fp, midpoint, tol, Nmax)
        count = count + newton_portion
        return[pstar, ier, count]
      else:
        #check for error
        if (fa*fc<0):
          b = c
        elif (fb*fc<0):
          a = c
          fa = fc
        else:
          pstar = c
          ier = 3
          return [pstar, ier, count]

        if (abs(b-a)<tol):
          pstar = a
          ier =0
          return [pstar, ier, count]        
        count = count +1

    astar = a
    ier = 2
    return [pstar,ier, count]

#The codes for question 6 using different methods 
# question 1 : the bisection method
# question 2 : the newton method
# question 3 : hybrid method

question1()
question2()
question3()





