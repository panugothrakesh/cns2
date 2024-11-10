def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The GCD of", a, "and", b, "is:", euclidean_gcd(a, b))
