import numpy as np
import numpy.linalg as la


def question1():
    a = -5
    b = 5
    f = lambda x: 1/(1+x**2)
    tol = 10e-4
    n_trap = 41
    n_simp = 107
    I_trap, x_trap, w_trap = traprule(a,b,f,n_trap)
    I_simp, x_simp, w_simp = simprule(a,b,f,n_simp)

    print('The trapezodial rule Tn comes to', I_trap)
    print('The simpsons rule comes to', I_simp)
    





def traprule(a,b,f,n):
  x = np.linspace(a,b,n)
  h = (b-a)/(n-1)
  w = h*np.ones(n)
  w[0]=0.5*w[0]
  w[n-1]=0.5*w[n-1]

  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

def simprule(a,b,f,n):
  x = np.linspace(a,b,n)
  h = (b-a)/(n-1)
  # Explain why this defines the weights for Simpsons
  w = (h/3)*np.ones(n)
  w[1:n:2]=4*w[1:n:2]
  w[2:n-1:2]=2*w[2:n-1:2]

  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

question1()