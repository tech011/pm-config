x, y = 0, 0  
h = 0.05  

def f(x, y):
    return y**2 + 1  

for _ in range(1):
    y = y + h * f(x, y)  
    x = x + h  

print("Approximate value of y at x =", round(x, 2), "is", round(y, 4))
