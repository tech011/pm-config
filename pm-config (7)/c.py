import numpy as np

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])
    return integral

f = np.cos
a, b = 0, 1
n = 5

result = trapezoidal_rule(f, a, b, n)
print("Estimated integral:", result)
