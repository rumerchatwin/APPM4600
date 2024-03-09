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
def evalJ(xvector): 
    x = xvector[0]
    y = xvector[1]

    J = np.array([[6*x , -2*y], [ 3*y**2 - 3*x**2, 6*x*y]])

    return [J]

def evalF(xvector):
    x = xvector[0]
    y = xvector[1]

    f = 3*x**2 - y**2
    g = 3*x*y**2 - x**3 - 1
    F = np.array([[f], [g]])
    
    return [F]

def question1c():
    x0 = 1
    y0 = 1
    xvector = np.array([[x0], [y0]])

    Nmax = 10
    tol = 10E-4

    [vector, ier, its] = Newton(xvector, tol, Nmax)
    print('The Newton method is', vector)

def Newton(xvector, tol, Nmax):

    for its in range(Nmax):
       J = evalJ(xvector)
       Jinv = inv(J)
       F = evalF(xvector)
       
       print ('This is J inverse dot F', Jinv.dot(F))

       x1vector = xvector - Jinv.dot(F)
       
       if (norm(x1vector - xvector) < tol):
           xstar = x1vector
           ier =0
           return[xstar, ier, its]
           
       xvector = x1vector
       print('This is the new xvector', xvector)
    
    xstar = x1vector
    ier = 1
    return[xstar,ier,its]


#question1a()
question1c()




