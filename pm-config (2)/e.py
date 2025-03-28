def sqrt(n):
    x = n
    y = 1
    while x - y > 0.0001:
        x = (x + y) / 2
        y = n / x
    return x

for num in range(21, 50):
    print("Square root of", num, "is", sqrt(num))
