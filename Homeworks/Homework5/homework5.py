import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def question4():
    x = np.arange(0, 5, 1)
    xp = np.array([0, 1, 2, 3])
    yp = np.array([1, 4, 2, 6])
    p1_x = lambda x: 13/10 + (13/10)*x
    p1 = p1_x(x)
    p2_x = lambda x: (1.257) + (1.2427)*x
    p2 = p2_x(x)
    plt.plot(x, p1, label = 'part a')
    plt.plot(x, p2, label = 'weighted')
    plt.plot(xp, yp, 'bo')
    plt.legend()
    plt.show()


def question3():
    x5 = np.linspace(0, (2*np.pi/9), 5)
    f5 = np.sin(9*x5)
    cs5 = CubicSpline(x5, f5, bc_type= 'periodic')
    err5 = abs(f5 - cs5(x5))

    x10 = np.linspace(0, (2*np.pi/9), 10)
    f10 = np.sin(9*x10)
    cs10 = CubicSpline(x10, f10 )
    err10 = abs(f10 - cs10(x10))

    x20 = np.linspace(0, (2*np.pi/9), 20)
    f20 = np.sin(9*x20)
    cs20 = CubicSpline(x20, f20, bc_type= 'periodic')
    err20 = abs(f20 - cs20(x20))

    x40 = np.linspace(0, (2*np.pi/9), 40)
    f40 = np.sin(9*x40)
    cs40 = CubicSpline(x40, f40, bc_type= 'periodic')
    err40 = abs(f40 - cs40(x40))


    plt.plot(x5, cs5(x5), label = 'n = 5')
    plt.plot(x10, cs10(x10), label = 'n = 10')
    plt.plot(x20, cs20(x20), label = 'n = 20')
    plt.plot(x40, cs40(x40), label = 'n = 40')
    plt.legend()
    plt.show()


question3()
    













#question4()