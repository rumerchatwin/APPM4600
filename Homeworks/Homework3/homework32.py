import numpy as np
import matplotlib.pyplot as plt

def driver():
  
# use routines    
    f = lambda x: 2*x - np.sin(x) - 1
    a = 0
    b = 1

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-9

    [astar,ier, count] = bisection(f,a,b,tol)
    #print('the approximate root is',astar)
    #print('the error message reads:',ier)
    #print('f(astar) =', f(astar))
    #print('The iterations is', count)

# Homework #3 question 2
def question2():
  f = lambda x: (x-5)**9
  a = 4.82
  b = 5.2
  tol = 1E-4

  [astar,ier, count] = bisection(f,a,b,tol)
  print('the approximate root is',astar)
  print('the error message reads:',ier)
  print('f(astar) =', f(astar))
  print('The iterations is', count)

  f_expanded = lambda x: x**9 -45*x**8 + 900*x**7 - 10500*x**6 + 78750*x**5 - 393750*x**4 + 1312500*x**3 - 2812500*x**2 + 3515625*x - 1953125

  [astar,ier,count] = bisection(f_expanded,a,b,tol)
  print('the approximate root of the exapnded function is',astar)
  print('the error message of the exapnded function reads:',ier)
  print('f(astar) of the exapnded function =', f(astar))
  print('The iterations of the exapnded function is', count)

# Question #3
def question3():
   f = lambda x: x**3 +x -4
   a = 1
   b = 4
   tol = 10**-3
   
   [astar,ier, count] = bisection(f,a,b,tol)
   print('the approximate root is',astar)
   print('the error message reads:',ier)
   print('f(astar) =', f(astar))
   print('The iterations is', count)

#Question 5
def question5a():
   x = np.linspace(-10, 10, 100)
   f =  x - 4 * np.sin(2*x) - 3
   plt.figure(1)
   plt.plot(x, f)
   plt.axhline(y=0, color = 'black')
   plt.axvline(x=0, color = 'black')
   plt.xlim(-2,8)
   plt.show()

#Question 5b
def question5b():
   f = lambda x: - np.sin(2*x) + ((5 * x) / 4) - (3/4)
   Nmax = 100
   x0 = -1
   tol = 10**-11
   [xstar, ier] = fixedpoint(f, x0, tol, Nmax)
   print('The approximated fixed point (1) is', xstar)
   print('The error (1) is', ier)
   x02 = -0.5
   [xstar2, ier2] = fixedpoint(f, x02, tol, Nmax)
   print('The approximated fixed point (2) is', xstar2)
   print('The error (2) is', ier2)
   x03 = 1.75
   [xstar3, ier3] = fixedpoint(f, x03, tol, Nmax)
   print('The approximated fixed point (3) is', xstar3)
   print('The error is', ier3)
   x04 = 3
   [xstar4, ier4] = fixedpoint(f, x04, tol, Nmax)
   print('The approximated fixed point (4) is', xstar4)
   print('The error is', ier4)
   x05 = 4.5
   [xstar5, ier5] = fixedpoint(f, x05, tol, Nmax)
   print('The approximated fixed point (5) is', xstar5)
   print('The error is', ier5)
  
def fixedpoint(f, x0, tol, nmax):
  count = 0
  while (count < nmax):
        x1 = f(x0)
        count = count + 1
        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return [xstar,ier]
        x0 = x1

  xstar = x1
  ier = 1
  return [xstar, ier]




# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b)
    count = 0
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier,count]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, count]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, count]

    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier,count]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      astar = d
      ier = 0
      return [astar, ier,count]
      

#driver()               
#question2()
#question3()
question5a()
question5b()


