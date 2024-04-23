import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time as time

def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 100
 
     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)
     t_start = time.perf_counter()
     x = scila.solve(A,b)
     t_stop = time.perf_counter()
     time0 = t_stop - t_start
     test = np.matmul(A,x)
     r = la.norm(test-b)
     
     ''' Exercise 3.2: Question 1'''
     t1_start = time.perf_counter()
     lu, piv = scila.lu_factor(A)
     t1_stop = time.perf_counter()

     t2_start = time.perf_counter()
     x = scila.lu_solve((lu, piv), b)
     t2_stop = time.perf_counter()

     time1 = t1_stop - t1_start
     time2 = t2_stop - t2_start

     print('Time for method 1:', time0)

def exercise():
     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)





     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
          
  
driver()   
