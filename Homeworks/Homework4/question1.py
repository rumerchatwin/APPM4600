import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
from numpy.linalg import inv 
from numpy.linalg import norm 

def question1a():
    f = lambda x, y: 3*x**2 - y**2
    g = lambda x, y: 3*x*y**2 - x**3 - 1

    x0 = 1
    y0 = 1
    N = 30
    tol = 10E-6
    x = np.zeros(N)
    y = np.zeros(N)
    matrix = [[1/6, 1/18], [0, 1/6]]
    for i in range(N):
        xvector = [[x0], [y0]]
        funcvector = [[f(x0, y0)], [g(x0, y0)]]
        result = xvector - np.dot(matrix, funcvector)

        x[i] = result[0]
        y[i] = result[1]

        x0 = x[i]
        y0 = y[i]
    
    answer = [[x], [y]]
    print('The x,y values are', answer)
    print('')
    print('The x-values are', answer[0])
    print('')
    print('The y-values are', answer[1])

# For Question 1c
def question1c():
    x0 = 1
    y0 = 1
    N = 50
    tol = 10E-6
    [xstar, i] = Newton( x0, y0, tol, N)
    print('The answer is', xstar)
    print('It took', i)


#finding the F array first
def findF(x, y):
    row1 = 3*x**2 - y**2
    row2 = 3*x*y**2 - x**3 - 1
    F = np.array([[row1],
                  [row2]])
    return(F)

#Finding the Jacobian 
def findJ(x,y):
    r1c1 = 6*x
    r1c2 = -2*y
    r2c1 = 3*y**2 - 3*x**2
    r2c2 = 6*x*y 
    J = np.array([[r1c1, r1c2],
                  [r2c1, r1c2]])
    return(J)


#Defining Newtons method for 2x2 matrix
def Newton(x0, y0, tol, Nmax):
    i = 1
    while (i <= Nmax):
        xvector = np.array([[x0],[y0]])
        F = findF(x0, y0)
        J = findJ(x0, y0)
        Jinv = inv(J)

        x1 = np.array(xvector - np.dot(Jinv, F), dtype=float)
        if (norm(x1-xvector) < tol):
            xfinal = x1
            return[xfinal, i]
        
        x0 = x1[0][0]
        y0 = x1[1][0]
        i += 1
        
    xfinal = xvector
    return[xfinal,i]
        

question1c()

