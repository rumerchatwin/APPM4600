import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

# define routines
def evalF(x): 

    #F = np.zeros(3)
    
    #F[0] = 3*x[0]-math.cos(x[1]*x[2])-1/2
    #F[1] = x[0]-81*(x[1]+0.1)**2+math.sin(x[2])+1.06
    #F[2] = np.exp(-x[0]*x[1])+20*x[2]+(10*math.pi-3)/3

    F = np.zeros(2)
    F[0] = 4 * x[0]**2 + x[1]**2 -4
    F[1] = x[0] + x[1] - math.sin(x[0] - x[1])
    return [F]
    
def evalJ(x): 
    J = np.array([[3.0, x[2]*math.sin(x[1]*x[2]), x[1]*math.sin(x[1]*x[2])], 
        [2.*x[0], -162.*(x[1]+0.1), math.cos(x[2])], 
        [-x[1]*np.exp(-x[0]*x[1]), -x[0]*np.exp(-x[0]*x[1]), 20]])
    J = np.array([[8*x[0] , 2*x[1]],
                 [1 - math.cos(x[0] - x[1]) , x[1] + math.cos(x[0] - x[1])]])

    return [J]

def driver():
    xo = np.array([[1],
                  [0]])
    tol = 10E-10
    Nmax = 100
    t = time.time()

    for j in range(20):
        [xstar,ier,its] =  Newton(xo,tol,Nmax)
        elapsed = time.time()-t
        print(xstar)
        print('Newton: the error message reads:',ier)
        print('Newton: took this many seconds:',elapsed/20)
        print('Netwon: number of iterations is:',its)
    
    for j in range(20):
        [xstar,ier,its] =  LazyNewton(xo,tol,Nmax)
        elapsed = time.time()-t
        print(xstar)
        print('Lazy Newton: the error message reads:',ier)
        print('Lazy Newton: took this many seconds:',elapsed/20)
        print('Lazy Newton: number of iterations is:',its)

    for j in range(20):
        [xstar,ier,its] =  SlackerNewton(xo,tol,Nmax)
        elapsed = time.time()-t
        print(xstar)
        print('Lazy Newton: the error message reads:',ier)
        print('Lazy Newton: took this many seconds:',elapsed/20)
        print('Lazy Newton: number of iterations is:',its)


def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]
           
def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]   

# Lab 6
def SlackerNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    J = evalJ(x0)
    Jinv = inv(J)
    new_inverse = 0

    for its in range(Nmax):
       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)

       if(abs(norm(evalF(x1))) > abs(norm(evalF(x0)))):
           Jinv = inv(Jinv)
           new_inverse =+ 1

       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its,new_inverse]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its,new_inverse]   


driver()
