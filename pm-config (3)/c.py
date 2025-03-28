import math

def f(x):
    return 1 / (1 + x)

a, b, n = 2, 10, 5  
h = (b - a) / n  

sum_mid = 0  
for i in range(1, n):
    sum_mid += f(a + i * h)

integral = (h / 2) * (f(a) + f(b) + 2 * sum_mid)
print("Estimated integral value:", round(integral, 4))


