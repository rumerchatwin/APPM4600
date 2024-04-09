import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math


def trap(a, b, f, N):
    h = (b - a)/N

    for j in range(1, N-1):
        x = a + j*h
        trap = trap + f(x) 
    trapezodial = h/2 * (f(a) + (2*trap) + f(b))
    return(trapezodial)


