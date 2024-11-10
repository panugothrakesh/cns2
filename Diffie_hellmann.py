def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p
def main():
    P = int(input("Enter the prime number P: "))
    G = int(input("Enter the primitive root G: "))
    a = int(input("Enter Alice's private key a: "))
    b = int(input("Enter Bob's private key b: "))
    x = power(G, a, P)
    y = power(G, b, P)
    ka = power(y, a, P)
    kb = power(x, b, P)
    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)
if __name__ == "__main__":
    main()