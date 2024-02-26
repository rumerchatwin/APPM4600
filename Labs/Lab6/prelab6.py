import numpy as np

#prelab 6
def driver():
    f = lambda x: np.cos(x)
    h = - np.arange(0, 10)
    nmax = 100
    tol = 10e10
    
    x0 = np.pi/2

    [f_der, f_ier, f_vector] = foward_difference(f, x0, h, nmax, tol)
    print('The foward difference is', f_der)
    print('The vector is', f_vector)
    print('The error is', f_ier)

    [c_der, c_ier, c_vector] = centered_difference(f, x0, h, nmax, tol)
    print('The centered difference is', c_der)
    print('The vector is', c_vector)
    print('The error is', c_ier)



#define the foward difference
def foward_difference(f, x, h, nmax, tol):
    count = 0
    vector = []
    while count < nmax:
        f_prime = (f(x + h[count]) - f(x)) / h[count]
        vector.append(f_prime)
        count =+ 1
        if (f_prime < tol):
            derivative = f_prime
            ier = 0
            return [derivative, ier, vector]
    
    ier = 1
    return [f_prime, ier, vector]

def centered_difference(f, x, h, nmax, tol):
    count = 0
    vector = []
    
    while count < nmax:
        f_prime = (f(x + h[count]) - f(x - h[count])) / 2 * h[count]
        vector.append(f_prime)
        count =+ 1
        if (f_prime < tol):
            derivative = f_prime
            ier = 0
            return[derivative, ier, vector]
        
    ier = 1
    return[ derivative, ier, vector]



