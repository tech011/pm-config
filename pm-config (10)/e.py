x, y = 0, 0  
h = 0.1  

def f(x, y):
    return 1 + y**2  

for _ in range(5):
    y = y + h * f(x, y)  
    x = x + h  

print("Approximate value of y at x =", round(x, 2), "is", round(y, 4))
