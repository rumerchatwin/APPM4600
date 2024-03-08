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


def evalJ(x, y): 
    J = np.array([[6*x , -2*y], [ 3*y**2 - 3*x**2, 6*x*y]]) 

    return [J]
def evalF(x, y):
    F = np.zeros(2)
    F[0] = 3*x**2 - y**2
    F[1] = 3*x*y**2 - x**3 - 1
    return [F]

def question1c():
    x0 = 1
    y0 = 1
    f = lambda x, y: 3*x**2 - y**2
    g = lambda x, y: 3*x*y**2 - x**3 - 1
    xvector = [[x0], [y0]]

    Nmax = 100
    tol = 10E-6

    [vector, ier, its] = Newton(xvector, F, J, tol, Nmax)
    print('The Newton method iteration has the vector as', vector)
    print('')
    print('The x-values are', vector[0])
    print('')
    print('The y-values are', vector[1])

def Newton(x0, y0, tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       x0vector = np.array([[x0], [y0]])
       J = evalJ(x0, y0)
       Jinv = inv(J)
       F = evalF(x0, y0)
       
       x1vector = x0vector - Jinv.dot(F)
       
       if (norm(x1vector-x0vector) < tol):
           xstar = x1vector
           ier =0
           return[xstar, ier, its]
           
       x0vector = x1vector
    
    xstar = x1vector
    ier = 1
    return[xstar,ier,its]


question1a()
question1c()
    


