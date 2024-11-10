def gcd_ext(a, b):
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while b:
        q = a // b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        a, b = b, a % b
    return a, x0, y0
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd, x, y = gcd_ext(a, b)
print(f"The GCD of {a} and {b} is {gcd}")
print(f"Coefficients x and y are: x = {x}, y = {y}")