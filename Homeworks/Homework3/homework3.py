import numpy as np

def problem3(x):
    y = np.e**x
    value = y - 1
    return value

x1 = 4.5
ystar = problem3(x1)

print ('ystar1 is', ystar)