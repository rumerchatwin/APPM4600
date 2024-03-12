import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def line(x0, x1, f, alpha):
    point1 = f(x0)
    point2 = f(x1)

    slope = (f(x1)-f(x0))/(x1-x0)
    y_intercept = (slope * x1) - x0
    linear_function = lambda x: slope*x + y_intercept

    alpha_function = linear_function(alpha)

    return(alpha_function)
