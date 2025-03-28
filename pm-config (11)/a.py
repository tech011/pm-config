def f(x):
    return x**2 - 50  

def df(x):  
    return 2*x  

x = 7  

while True:
    x_new = x - f(x) / df(x)
    if abs(x_new - x) < 0.0001:  
        break
    x = x_new  

print("Approximate root:", round(x, 4))
