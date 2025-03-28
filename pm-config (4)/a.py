def f(x):
    return 3*x**2 + 4*x - 10

a, b = 1, 2  

while True:
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))  
    if f(c) < 0:
        a = c
    else:
        b = c

    if abs(f(c)) < 0.0001:
        break  

print("Approximate root:", round(c, 4))
