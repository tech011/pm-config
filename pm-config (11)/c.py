def exp(x):
    sum_exp = 1  
    term = 1  
    for i in range(1, 20):
        term = term * x / i  
        sum_exp = sum_exp + term  
    return sum_exp  

a, b, n = 0, 6, 6  
h = (b - a) / n  

sum1 = 0  
sum2 = 0  

for i in range(1, n, 2):
    sum1 = sum1 + exp(a + i * h)

for i in range(2, n-1, 2):
    sum2 = sum2 + exp(a + i * h)

integral = (h / 3) * (exp(a) + exp(b) + 4 * sum1 + 2 * sum2)
print("Integral value:", round(integral, 4))
