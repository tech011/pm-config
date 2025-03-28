import math

def f(x):
    return 3*x - math.cos(x) - 1  

def df(x):
    return 3 + math.sin(x)  

x = 0.5  

while True:
    x_new = x - f(x) / df(x)
    if abs(x_new - x) < 0.0001:  
        break
    x = x_new  

print("Approximate root:", round(x, 4))
