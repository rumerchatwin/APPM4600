import numpy as np

def driver():
    f = lambda x: np.cos(x)
    x0 = np.pi/2
    h = 0.01 / 2 ** np.arange(0,10)

    foward_derivative = foward(f, h, x0)
    centered_derivative = centered(f,h,x0)
    print('The foward difference approximation', foward_derivative)
    print('The centered difference approximation is', centered_derivative)

def foward(f, h, x0):
    derivative = (f(x0 + h) - f(x0)) / h
    return[derivative]
def centered(f, h, x0):
    derivative = (f(x0 + h) - f(x0 - h))/ (2 * h)
    return[derivative]

driver()
