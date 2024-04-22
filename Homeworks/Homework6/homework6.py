import numpy as np
import numpy.linalg as la
from adaptive_quad import *

def question1():
    a = -5
    b = 5
    f = lambda x: 1/(1+x**2)
    tol = 10e-4
    



def traprule(a,b,f,n):
  x = np.linspace(a,b,n)
  h = (b-a)/(n-1)
  w = h*np.ones(n)
  w[0]=0.5*w[0]
  w[n-1]=0.5*w[n-1]

  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

def eval_composite_simpsons(n,a,b,f):
  x = np.linspace(a,b,n)
  h = (b-a)/(n-1)
  # Explain why this defines the weights for Simpsons
  w = (h/3)*np.ones(n)
  w[1:n:2]=4*w[1:n:2]
  w[2:n-1:2]=2*w[2:n-1:2]

  I_hat = np.sum(f(x)*w)
  return I_hat,x,w