def euler_method(f, x0, y0, h, x_target):
    x, y = x0, y0
    while x > x_target:
        y_next = y + h * f(x, y)
        if abs(y_next) > 1e6:  
            print("Numerical instability detected. Stopping computation.")
            return None
        y = y_next
        x -= h  
    return y

def f(x, y):
    return -x * y**2

x0, y0 = 2, 1
h = 0.01  
x_target = 0.6

y_result = euler_method(f, x0, y0, h, x_target)
if y_result is not None:
    print(f"y({x_target}) ≈ {y_result}")
