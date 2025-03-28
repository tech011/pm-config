x, y = 0, 1  
h = 0.01  

def f(x, y):
    return -y  

for _ in range(4):
    y = y + h * f(x, y)  
    x = x + h  

print("Approximate value of y at x =", round(x, 2), "is", round(y, 4))
