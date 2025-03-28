def f(x):
    return x**3 - 8*x - 4  

def df(x):  
    return 3*x**2 - 8  

x = 2.0  

while True:
    x_new = x - f(x) / df(x)
    if abs(x_new - x) < 0.0001:  
        break
    x = x_new  

print("Approximate root:", round(x, 4))
