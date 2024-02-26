import numpy as np

#prelab 6
def driver():
    f = lambda x: np.cos(x)
    h = - np.arange(0, 10) * 2 
    
    x0 = np.pi/2

    [f_der, f_vector] = foward_difference(f, x0, h)
    print('The foward difference is', f_der)
    print('The vector is', f_vector)

    [c_der, c_vector] = centered_difference(f, x0, h)
    print('The centered difference is', c_der)
    print('The vector is', c_vector)



#define the foward difference
def foward_difference(f, x, h):
    count = 0
    vector = []
    while count <= len(h):
        f_prime = (f(x + h[count]) - f(x)) / h[count]
        vector.append(f_prime)
        count =+ 1

    return [f_prime, vector]

def centered_difference(f, x, h):
    count = 0
    vector = []
    
    while count <= len(h):
        f_prime = (f(x + h[count]) - f(x - h[count])) / 2 * h[count]
        vector.append(f_prime)
        count =+ 1

    return[f_prime, vector]
        


driver()

