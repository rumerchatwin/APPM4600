# get lgwts routine and numpy
import numpy as np;
import numpy.linalg as la;
from gauss_legendre import *;
from scipy import integrate
# adaptive quad subroutines
# the following three can be passed
# as the method parameter to the main adaptive_quad() function

def driver():
    a = -5
    b = 5
    f = lambda x: 1/(1+x**2)
    tol = 10e-4
    n_trap = 41
    n_simp = 107
    method_trap = eval_composite_trap
    method_simp = eval_composite_simpsons
    method_quad = eval_gauss_quad

    (I_trap, uniquex, nsplit_trap) = adaptive_quad(a, b, f, tol, n_trap, method_trap)
    print('The I for trap method is', I_trap)
    print('The nsplit is', nsplit_trap)

    (I_simp, uniquex_simp, nsplit_simp) = adaptive_quad(a, b, f, tol, n_simp, method_simp)
    print('The I for simpson method is', I_simp)
    print('The nsplit is', nsplit_simp)

    quad1 = integrate.quad(f, a, b, epsrel = 10e-4)
    quad2 = integrate.quad(f, a, b, epsrel = 10e-6)
    print('The scipy quad version with 10e-4 is', quad1)
    print('The scipy quad version with 10e-6 is', quad2)



def eval_composite_trap(M,a,b,f):
  x = np.linspace(a,b,M)
  h = (b-a)/(M-1)
  w = h*np.ones(M)
  w[0]=0.5*w[0]
  w[M-1]=0.5*w[M-1]

  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

def eval_composite_simpsons(M,a,b,f):
  x = np.linspace(a,b,M)
  h = (b-a)/(M-1)
  # Explain why this defines the weights for Simpsons
  w = (h/3)*np.ones(M)
  w[1:M:2]=4*w[1:M:2]
  w[2:M-1:2]=2*w[2:M-1:2]

  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

def eval_gauss_quad(M,a,b,f):
  """
  Non-adaptive numerical integrator for \int_a^b f(x)w(x)dx
  Input:
    M - number of quadrature nodes
    a,b - interval [a,b]
    f - function to integrate

  Output:
    I_hat - approx integral
    x - quadrature nodes
    w - quadrature weights

  Currently uses Gauss-Legendre rule
  """
  x,w = lgwt(M,a,b)
  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

def adaptive_quad(a,b,f,tol,M,method):
  """
  Adaptive numerical integrator for \int_a^b f(x)dx

  Input:
  a,b - interval [a,b]
  f - function to integrate
  tol - absolute accuracy goal
  M - number of quadrature nodes per bisected interval
  method - function handle for integrating on subinterval
         - eg) eval_gauss_quad, eval_composite_simpsons etc.

  Output: I - the approximate integral
          X - final adapted grid nodes
          nsplit - number of interval splits
  """
  # 1/2^50 ~ 1e-15
  maxit = 50
  left_p = np.zeros((maxit,))
  right_p = np.zeros((maxit,))
  s = np.zeros((maxit,1))
  left_p[0] = a; right_p[0] = b
  # initial approx and grid
  s[0],x,_ = method(M,a,b,f)
  # save grid
  X = []
  X.append(x)
  j = 1
  I = 0
  nsplit = 1
  while j < maxit:
    # get midpoint to split interval into left and right
    c = 0.5*(left_p[j-1]+right_p[j-1])
    # compute integral on left and right spilt intervals
    s1,x,_ = method(M,left_p[j-1],c,f); X.append(x)
    s2,x,_ = method(M,c,right_p[j-1],f); X.append(x)

    if np.max(np.abs(s1+s2-s[j-1])) > tol:
      left_p[j] = left_p[j-1]
      right_p[j] = 0.5*(left_p[j-1]+right_p[j-1])
      s[j] = s1
      left_p[j-1] = 0.5*(left_p[j-1]+right_p[j-1])
      s[j-1] = s2
      j = j+1
      nsplit = nsplit+1
    else:
      I = I+s1+s2
      j = j-1
      if j == 0:
        j = maxit
  return I,np.unique(X),nsplit

