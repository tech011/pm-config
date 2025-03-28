x, y = 1, 1  
h = 0.1  

def f(x, y):
    return x + y**2  

for _ in range(6):
    y = y + h * f(x, y)  
    x = x + h  

print("Approximate value of y at x =", round(x, 2), "is", round(y, 4))
