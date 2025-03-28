import numpy as np

def f(x):
    return np.sin(x)

def simpsons_rule(a, b, n):
    if n % 2 == 1:
        raise ValueError("n must be even for Simpson's rule")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    integral = y[0] + y[-1] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2])
    integral *= h / 3
    
    return integral

a, b = 0, np.pi
n = 6

result = simpsons_rule(a, b, n)
print("Estimated integral:", result)
