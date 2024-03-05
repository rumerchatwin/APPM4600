# Lab 7
import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():
    f = lambda x: 1/(1+(10*x)**2)
    N = 10
    h = 2/(N-1)

