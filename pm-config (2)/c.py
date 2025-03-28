import numpy as np

def g(x):
    return 1 / (1 + x**2)

def simpsons_rule(a, b, n, func):
    if n % 2 == 1:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    
    integral = y[0] + y[-1] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2])
    integral *= h / 3
    
    return integral

a = 0
b = 1
n = 4

result_g = simpsons_rule(a, b, n, g)
print("Estimated integral of 1/(1+x^2):", result_g)
