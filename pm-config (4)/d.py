def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a  

for num in range(1, 150):
    if gcd(num, 111) == 1:
        print(num, end=" ")
