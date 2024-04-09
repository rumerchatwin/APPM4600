import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math

def trapezodial(a, b, f, N):
    x0 = a
    x1 = b
    x = np.zeros(N)
    x[0] = x0
    x[N-1] = x1

    for i in range(a, N-1):
        h = x[i] - x[i-1]
        trap = trap + (1/2) * ( (x[i] - x[i-1]) * (f(x[i-1]) + f(x[i])))

    return(trap)

def simpson(a, b, f, N):
    x0 = a
    x2 = b
    h = (b-a)/2
    x1 = a + h

    simp = (h/3) * ( f(x0) + 4*f(x1) + f(x2))
    return(simp)
