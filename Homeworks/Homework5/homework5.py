import numpy as np
import matplotlib.pyplot as plt



def question4():
    x = np.arange(0, 5, 1)
    xp = np.array([0 1 2 3])
    yp = np.array([1, 4, 2, 6])
    p1_x = lambda x: 13/10 + (13/10)*x
    p1 = p1_x(x)
    p2_x = lambda x: ((4*np.sqrt(2) + 7*np.sqrt(3))/ 10*np.sqrt(2)) + ((2*np.sqrt(2) - 7*np.sqrt(3))/(10*np.sqrt(2)))*x
    p2 = p2_x(x)
    plt.plot(x, p1, label = 'part a')
    plt.plot(x, p2, label = 'weighted')
    plt.plot(xp, yp, 'bo')
    plt.legend()
    plt.show()

question4()