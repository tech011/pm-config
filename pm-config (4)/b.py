x_values = [1, 2, 3, 4, 5]
y_values = [41, 62, 65, 50, 17]
h = x_values[1] - x_values[0]

f_n = y_values[-1]
f_n_1 = y_values[-2]
f_n_2 = y_values[-3]
f_n_3 = y_values[-4]

d1 = f_n - f_n_1  
d2 = f_n_1 - f_n_2  
d3 = f_n_2 - f_n_3  

d1_2 = d1 - d2  
d2_2 = d2 - d3  

d1_3 = d1_2 - d2_2  

x = 3.5  
p = (x - x_values[-1]) / h  

f_x = f_n + p*d1 + (p*(p+1)*d1_2)/2 + (p*(p+1)*(p+2)*d1_3)/6  

print("Interpolated value at x =", x, "is", round(f_x, 4))
