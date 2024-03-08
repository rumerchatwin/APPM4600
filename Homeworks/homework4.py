import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
from numpy.linalg import inv 


def question1a():
    f = lambda x, y: 3*x**2 - y**2
    g = lambda x, y: 3*x*y**2 - x**3 - 1

    x0 = 1
    y0 = 1
    N = 20
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

    
    

question1a()
    


