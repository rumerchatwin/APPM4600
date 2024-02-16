# APPM 4600
# Rumer Chatwin
import numpy as np 
import matplotlib.pyplot as plt

# Question a
# creating a vector t at 0 to pi with increments of pi/30
t = np.arange(0, np.pi, np.pi/30)
# create a vector for y
y1 = np.cos(t)

N = len(t)
k = 1

for k in range(N):
    S = t[k] * y1[k]
    k = k + 1
print('the sum is', S)

# Question b
# Create variables for first plot
theta = np.linspace(0, 2*np.pi, num = 100000)
R = 1.2
Sr = 0.1
f = 15
p = 0

x = R * np.cos(theta) * (1 + Sr * np.sin(f * theta + p)) 
y = R * np.sin(theta) * (1 + Sr * np.sin(f * theta + p)) 
#create plots
plt.figure(1)
plt.plot(x,y)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()


#create varibles for plot 2
Sr2 = 0.05
p2 = np.random.uniform(0, 2)

plt.figure(2)
for i in range(10):
    R2 = i
    f = 2 + i
    x2 = R2 * np.cos(theta) * (1 + Sr2 * np.sin(f * theta + p2)) 
    y2 = R2 * np.sin(theta) * (1 + Sr2 * np.sin(f * theta + p2))
    plt.plot(x2, y2)
    i = i + 1
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()



