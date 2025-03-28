def f(x):
    return 2*x**2 - 4*x - 1

a, b, n = 2, 4, 5  
h = (b - a) / n  

sum_mid = 0  

for i in range(1, n):
    sum_mid = sum_mid + f(a + i * h)

integral = (h / 2) * (f(a) + f(b) + 2 * sum_mid)
print("Integral value:", round(integral, 4))
