# import math 

# gcd = math.gcd(98,70)
# print(gcd)


def find_gcd(a,b):
    while b != 0:
        a, b = b, a % b 
    return abs(a)
print("GCD is:", find_gcd(240,400))