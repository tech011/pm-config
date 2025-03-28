x_values = [150, 152, 154, 155]
y_values = [12.247, 12.329, 12.410, 12.490]
x = 153  
n = len(x_values)
f_x = 0  

for i in range(n):
    term = y_values[i]  
    for j in range(n):
        if i != j:
            term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
    f_x = f_x + term  

print("Interpolated value at x =", x, "is", round(f_x, 4))
