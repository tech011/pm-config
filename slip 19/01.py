x_values = [1, 2, 3, 4, 5]
y_values = [30, 50, 65, 40, 18]
h = x_values[1] - x_values[0]

f0 = y_values[0]
f1 = y_values[1]
f2 = y_values[2]
f3 = y_values[3]
f4 = y_values[4]

d1 = f1 - f0  
d2 = f2 - f1  
d3 = f3 - f2  
d4 = f4 - f3  

d1_2 = d2 - d1  
d2_2 = d3 - d2  
d3_2 = d4 - d3  

d1_3 = d2_2 - d1_2  
d2_3 = d3_2 - d2_2  

d1_4 = d2_3 - d1_3  

x = 1.5  
p = (x - x_values[0]) / h  

f_x = f0 + p*d1 + (p*(p-1)*d1_2)/2 + (p*(p-1)*(p-2)*d1_3)/6 + (p*(p-1)*(p-2)*(p-3)*d1_4)/24

print("Interpolated value at x =", x, "is", round(f_x, 4))
