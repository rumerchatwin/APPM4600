import numpy as np 

# creating a vector t at 0 to pi with increments of pi/30
t = np.arange(0, np.pi, np.pi/30)
# create a vector for y
y = np.cos(t)

N = np.range(t)
k = 1

for k in range(t):
    S = t[k] * y[k]
    k = k + 1
    print('the sum is', S)

