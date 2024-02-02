import numpy as np
import matplotlib.pyplot as plt
import math

#Question #1 on the Homework

x = np.arange(1.920, 2.080, 0.001)
y = x**9 - (18*x**8) + (144*x**7) - (672*x**6) + (2016*x**5) - (4032*x**4) + (5376*x**3) - (4608*x**2) + (2304*x) - 512
#plt.plot(x,y)

l = (x-2)**9
#plt.plot(x,l)

#Question 5 on the homework

# part 1

x = np.pi
y = np.array([10**-16, 10**-15, 10**-14, 10**-13, 10**-12, 10**-11, 10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0])
w = np.cos(x + y) - np.cos(x)

#plt.plot(y, w, label = 'cos(x+ sigma) + cos(x)', color = 'black')

numerator = 2 * (np.cos(x))**2 * (np.sin(y))**2
denominator = np.cos(x+y) + np.cos(x)

w2 = numerator / denominator

#plt.plot(y, w2, label = 'my expression', color = 'red')

#difference = w - w2
#plt.plot(y, difference, label = 'difference', color = 'blue')

w3 = -y * np.sin(x) - (y**2 / 2) * np.cos(x)
#plt.plot (y, w3, label = 'problem d', color = 'purple')


#plt.title('x=pi')
#plt.legend()

# part 2

x = 10**6
y = np.array([10**-16, 10**-15, 10**-14, 10**-13, 10**-12, 10**-11, 10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0])
w = np.cos(x + y) - np.cos(x)

#plt.plot(y, w, label = 'cos(x+ sigma) + cos(x)', color = 'black')

numerator = 2 * (np.cos(x))**2 * (np.sin(y))**2
denominator = np.cos(x+y) + np.cos(x)

w2 = numerator / denominator

#plt.plot(y, w2, label = 'my expression', color = 'red')

w3 = -y * np.sin(x) - (y**2 / 2) * np.cos(x + y)
#plt.plot (y, w3, label = 'problem d', color = 'purple')

#difference = w - w2
#plt.plot(y, difference, label = 'difference', color = 'blue')
#plt.title('x=10^6')
#plt.legend()

# part 3

x = np.pi
y = np.array([10**-16, 10**-15, 10**-14, 10**-13, 10**-12, 10**-11, 10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0])

w3 = -y * np.sin(x) - (y**2 / 2) * np.cos(x)
#plt.plot (y, w3, label = 'problem d', color = 'purple')

# part 4

x = np.pi
y = np.array([10**-16, 10**-15, 10**-14, 10**-13, 10**-12, 10**-11, 10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0])
w = np.cos(x + y) - np.cos(x)

#plt.plot(y, w, label = 'cos(x+ sigma) + cos(x)', color = 'black')

part1 = 0.5*(np.sin(x))**2 
part2 = np.sin(y) * np.sin(2*x) 
numerator = - part1 - part2
denominator = np.cos(x+y) + np.cos(x)

w2 = numerator / denominator

#plt.plot(y, w2, label = 'my expression', color = 'red')

#difference = w - w2
#plt.plot(y, difference, label = 'difference', color = 'blue')

#plt.title('x=pi')
#plt.legend()





