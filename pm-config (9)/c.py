def f(x):
    return 1 / (1 + x**2)

a, b, n = 0, 1, 4  
h = (b - a) / n  

sum1 = 0  
sum2 = 0  

for i in range(1, n, 2):
    sum1 = sum1 + f(a + i * h)

for i in range(2, n-1, 2):
    sum2 = sum2 + f(a + i * h)

integral = (h / 3) * (f(a) + f(b) + 4 * sum1 + 2 * sum2)
print("Integral value:", round(integral, 4))
