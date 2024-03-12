import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv

def line(x0, x1, f, alpha):
    point1 = f(x0)
    point2 = f(x1)

    slope = (f(x1)-f(x0))/(x1-x0)
    y_intercept = (slope * -x1) + point2
    linear_function = lambda x: slope*x + y_intercept

    alpha_function = linear_function(alpha)

    return(alpha_function)

def driver():
    f = lambda x: np.exp(x)
    a = 0
    b = 1
    Neval = 100
    xeval = np.linspace(a,b,Neval)
    Nint = 10
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    fex = f(xeval)

    plt.figure(1)
    plt.plot(xeval,fex,'ro-', label = 'fex')
    plt.plot(xeval,yeval,'bs-', label = 'yeval')
    plt.legend()
    plt.show()

    err = abs(yeval-fex)
    plt.figure(2)
    plt.plot(xeval,err,'ro-')
    plt.show()

def excercise32():
    f = lambda x: 1/(1 + (10*x)**2)
    a = 1
    b = -1
    Neval = 100
    xeval = np.linspace(a,b,Neval)
    Nint = 10
    yeval = eval_lin_spline(xeval, Neval, a , b, f, Nint)
    fex = f(xeval)

    plt.figure(1)
    plt.plot(xeval,fex,'ro-', label = 'fex')
    plt.plot(xeval,yeval,'bs-', label = 'yeval')
    plt.legend()
    plt.show()

    err = abs(yeval-fex)
    plt.figure(2)
    plt.plot(xeval,err,'ro-')
    plt.show()
    


def eval_lin_spline(xeval,Neval,a,b,f,Nint):

    xint = np.linspace(a,b,Nint+1)
    yeval = np.zeros(Neval)
    for jint in range(Nint):
        atmp = xint[jint]
        btmp = xint[jint+1]
        # find indices of values of xeval in the interval
        ind = np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]
        n = len(xloc)
        fa = f(atmp)
        fb = f(btmp)
        yloc = np.zeros(len(xloc))
        for kk in range(n):
            #use your line evaluator to evaluate the spline at each location
            yloc[kk] = line(atmp, btmp, f, kk)
            print(yloc[kk])
            # Copy yloc into the final vector
            yeval[ind] = yloc
    return yeval


#driver()
#excercise32()