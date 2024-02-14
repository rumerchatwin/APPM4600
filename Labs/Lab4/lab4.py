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
    [xstar, ier, p_vector] = fixedpt(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f1(xstar))
    print('Error message reads:',ier)
    print('the iterations are', p_vector)
    print('length', len(p_vector))
    #3.2 exercise 
    [pa_vector] = aitken(p_vector)
    print('The aitken method vector is', pa_vector)


#test f2 '''
    x0 = 0.0
    [xstar,ier,p_vector] = fixedpt(f2,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f2(xstar):',f2(xstar))
    print('Error message reads:',ier)
    print('the iterations are', p_vector)
    #3.2 exercise 
    [pa_vector] = aitken(p_vector)
    print('The aitken method vector is', pa_vector)


# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    p_vector = []
    count = 0
    while (count < Nmax):
        x1 = f(x0)
        p_vector.append(x1)
        count = count + 1
        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return [xstar,ier, p_vector]
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
                return[n]
        elif(n == 2):
            convergence = 2
            return[n]
    
    return[n]

#lab 4 : 3.1 Aitken's technique
def aitken(p_vector):
    
    pa_vector = []
    n = 1

    while n < (len(p_vector) - 2):     
        numerator = (p_vector[n+1] - p_vector[n])**2
        denominator = p_vector[n+2] - 2*p_vector[n+1] + p_vector[n]
        pa_vector.append(p_vector[n] - numerator/denominator)
        n = n + 1

    return[pa_vector]

#lab 4: 3.2 Excercise (Steffansons Method)
def steff(p0,g,tol,Nmax):
    
    a = p0
    p_vector = []
    n = 0

    while n < Nmax:
        b = g(a)
        c = g(b)
        value = a - ((b-a)**2)/(c -2*b + a)
        p_vector.append(value)
        if (abs(value - a) < tol):
            p = c
            ier = 0
            return [p , ier, p_vector]
        a = value
        n = n + 1
    p = b
    ier = 1
    return[p, ier, p_vector]

#driver()

# for lab4 question 2 in 3.4
Nmax = 100
g = lambda x: (10/(x+4))**0.5
p0 = 1.5
tol = 10E-10

[p, ier, p_vector] = steff(p0, g, tol, Nmax)
print('The value p is', p)
print('The error reads', ier)
print('The p vector is', p_vector)