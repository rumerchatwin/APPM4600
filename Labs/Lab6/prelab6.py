import numpy as np

f = lambda s: np.cos(s)
h = np.arange(0,10)
x = np.pi/2

foward = (f(x + h) - f(x)) / h
centered = (f(x + h) - f(x-h)) / 2 * h

derivative = -np.sin(x)

print('The Foward Difference apporximation is', foward)
print('The Centered Difference approximation is', centered)
print('The deriavtive is', derivative)
