import numpy as np
import matplotlib.pyplot as plt

def weight(xj,x):
    prod = 1
    for i in range(len(x)):
        if x[i] != xj:
            prod = prod * (xj - x[i])
    wj = 1/prod
    return(wj)

def eval_bary_lagrange(xeval,xint,yint):
    sum1 = 0
    sum2 = 0
    for j in range(len(xint)):
        if xeval != xint[j]:
            wj = weight(xint[j], xint)
            sum1 = sum1 + (wj * yint[j]) / (xeval - xint[j])
            sum2 = sum2 + wj / (xeval - xint[j])
    yeval = sum1/sum2
    return(yeval)

def eval_phi(xeval,xint):
    prod = 1
    for i in range (len(xint)):
        prod = prod * (xeval-xint[i])
    return(prod)

n = 15
N = 1000

h = 2/n
i = np.arange(1, n+2, 1)
xint = -1 + (i - 1)*h

j = np.arange(0, n+1, 1)
cheby_xint = np.cos(((2*j + 1)*np.pi) / (2*(n + 1)))
#print(cheby_xint)

xeval = np.linspace(-1,1,N)

f = lambda x: 1/(1 + (16*x)**2)

fex = f(xeval)
yint = f(xint)
cheby_yint = f(cheby_xint)

bary_lagrange1 = np.zeros(len(xeval))
bary_lagrange2 = np.zeros(len(xeval))

for j in range(len(xeval)):
    bary_lagrange1[j] = eval_bary_lagrange(xeval[j],xint,yint)
    bary_lagrange2[j] = eval_bary_lagrange(xeval[j],cheby_xint,cheby_yint)


plt.figure(1)
plt.plot(xint, yint, 'o', label = 'Equispaced Nodes')
plt.plot(cheby_xint, cheby_yint, 'o', label = 'Chebysehv Nodes')
plt.plot(xeval, fex, label = 'f(x)')
plt.plot(xeval, bary_lagrange1, label = 'Equispaced p(x)')
plt.plot(xeval, bary_lagrange2, label = 'Chebyshev p(x)')
plt.legend()
plt.show()

phi = np.zeros(len(xeval))
cheby_phi = np.zeros(len(xeval))

for j in range(len(xeval)):
    phi[j] = eval_phi(xeval[j], xint)
    cheby_phi[j] = eval_phi(xeval[j], cheby_xint)

plt.figure(2)
plt.semilogy(xeval, phi, label = 'Equispaced Nodes')
plt.semilogy(xeval, cheby_phi, label = 'Chebyshev Nodes')
plt.legend()
plt.show()