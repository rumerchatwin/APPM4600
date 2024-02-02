import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(1.920, 2.080, 0.001)
y = x**9 - (18*x**8) + (144*x**7) - (672*x**6) + (2016*x**5) - (4032*x**4) + (5376*x**3) - (4608*x**2) + (2304*x) - 512
plt.figure(1)
plt.plot(x,y)

plt.figure(2)
l = (x-2)**9
plt.plot(x,l)

