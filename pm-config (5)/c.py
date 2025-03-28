def f(x):
    return x**3

a, b, n = 1, 5, 6  
h = (b - a) / n  

sum1 = 0  
sum2 = 0  

for i in range(1, n, 3):
    sum1 = sum1 + f(a + i * h)

for i in range(2, n, 3):
    sum2 = sum2 + f(a + i * h)

integral = (3*h / 8) * (f(a) + f(b) + 3 * sum1 + 3 * sum2)
print("Integral value:", round(integral, 4))
