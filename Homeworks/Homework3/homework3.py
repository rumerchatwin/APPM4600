# APPM 4600
# Rumer Chatwin
import numpy as np 
import matplotlib.pyplot as plt

# Question a
# creating a vector t at 0 to pi with increments of pi/30
t = np.arange(0, np.pi, np.pi/30)
# create a vector for y
y = np.cos(t)

N = len(t)
k = 1

for k in range(len(t)):
    S = t[k] * y[k]
    k = k + 1
    print('the sum is', S)
    break

# Question b
# Create variables
theta = np.arange(0, np.pi, np.pi/2)
R = 1.2
Sr = 0.1
f =15
p = 0

x = R * (1 + Sr * np.sin(f * theta + p)) * np.cos(theta)
y = R * (1 + Sr * np.sin(f * theta + p)) * np.sin(theta)

#create plots
plt.figure()
plt.plot(theta, x, color = 'r')
plt.plot(theta, y, color = 'blue')
plt.show(block=False)