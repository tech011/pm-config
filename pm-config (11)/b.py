x_values = [0, 1, 2, 3]
y_values = [11, 10, 11, 21]
h = x_values[1] - x_values[0]

f0 = y_values[0]
f1 = y_values[1]
f2 = y_values[2]
f3 = y_values[3]

d1 = f1 - f0  
d2 = f2 - f1  
d3 = f3 - f2  

d1_2 = d2 - d1  
d2_2 = d3 - d2  

x = 2.4  
p = (x - x_values[0]) / h  

f_x = f0 + p*d1 + (p*(p-1)*d1_2)/2  

print("Interpolated value at x =", x, "is", round(f_x, 4))
