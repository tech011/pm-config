def f(x):
    return x**5 + 3*x + 1  

def df(x):  
    return 5*x**4 + 3  

x = -1.5  

while True:
    x_new = x - f(x) / df(x)
    if abs(x_new - x) < 0.0001:  
        break
    x = x_new  

print("Approximate root:", round(x, 4))
