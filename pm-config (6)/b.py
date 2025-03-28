x_values = [1, 2, 3, 4, 5]
y_values = [40, 60, 65, 50, 18]
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

print("Fourth order forward difference:", d1_4)
