import numpy as np
import time
import matplotlib.pyplot as plt
import numpy.linalg as la
from numpy.linalg import inv 
from numpy.linalg import norm 

''' Question 3 asks to solve the nonlinear system'''
''' The inital guess is x = 0, y = 0, and  z = 0'''
def driver():
    tol = 10E-6
    Nmax = 10
    x0 = 0; y0 = 0; z0= 0
    t = time.time()

    xfinal =  Newton(x0, y0, z0, tol,Nmax)
    print(xfinal)
    

''' Finding the matrix F and Jacobian matrix '''
def evalF(x, y, z):
    F = np.array([[x + np.cos(x * y * z) -1],
                  [(1 - x)**(1/4) + y + 0.05*z**2 - 0.12*z -1],
                  [-x**2 - 0.1*y**2 +z - 1]])
    
    return F   

def evalJ(x, y, z):
    J = np.array([[(1 - y*z*np.sin(x*y*z)), -x*z*np.sin(x*y*z), -x*y*np.sin(x*y*z)],
                  [(1/4)*(1-x)**(-3/4), 1, 0.1*z - 0.15],
                  [-2*x, -0.2*y + 0.01, 1] ])
    return J

''' First way: Newtons Methods '''
def Newton(x0, y0, z0, tol, Nmax):
    i = 1
    while (i <= Nmax):
        xvector = np.array([[x0],[y0],[z0]])
        F = evalF(x0, y0, z0)
        J = evalJ(x0, y0, z0)
        Jinv = inv(J)

        x1 = np.array(xvector - np.dot(Jinv, F), dtype=float)
        print(x1)
        if (norm(x1-xvector) < tol):
            xfinal = x1
            return(xfinal)
        
        x0 = x1[0][0]
        y0 = x1[1][0]
        z0 = x1[2][0]
        i += 1

    return(xfinal)
    
driver()

    

