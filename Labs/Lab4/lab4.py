# import libraries
import numpy as np
    
def driver():

# test functions 
    f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

    f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

    Nmax = 100
    tol = 1e-6


# test f1 '''
    x0 = 0.0
    [xstar,ier,p_vector] = fixedpt(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f1(xstar))
    print('Error message reads:',ier)
    print('the iterations are', p_vector)
    convergence = ooc(f1(xstar), p_vector)
#test f2 '''
    x0 = 0.0
    [xstar,ier,p_vector] = fixedpt(f2,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f2(xstar):',f2(xstar))
    print('Error message reads:',ier)
    print('the iterations are', p_vector)
    convergence2 = ooc(f2(xstar), p_vector)



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    p_vector = np.zeros((Nmax, 1))
    count = 0
    while (count < Nmax):
        x1 = f(x0)
        p_vector[count]= x1
        count = count + 1
        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return [xstar,ier,]
        x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier,p_vector]

def ooc(p, p_vector):
    n = 0
    convergence = 0
    while n in range(2):
        limit = abs(p_vector[n+1] - p) / abs(p_vector[n] - p)**n

        if (n == 1):
            if(limit < 1):
                print('Lineraly Converges')
        elif(n == 2):
            convergence = 2
            print('Quadraticaly convergent')

    if (convergence != 1):
        if(convergence !=2):
            print('error in convergence')

driver()