def f(x):
    return x**3 - 4*x - 9

a, b = 2, 3  

while True:
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))  
    if f(c) < 0:
        a = c
    else:
        b = c

    if abs(f(c)) < 0.0001:
        break  

print("Approximate root:", round(c, 4))
