x_values = [1, 2, 3, 4, 5]
y_values = [30, 50, 55, 40, 11]
x = 3.5  
n = len(x_values)
f_x = 0  

for i in range(n):
    term = y_values[i]  
    for j in range(n):
        if i != j:
            term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
    f_x = f_x + term  

print("Interpolated value at x =", x, "is", round(f_x, 4))
