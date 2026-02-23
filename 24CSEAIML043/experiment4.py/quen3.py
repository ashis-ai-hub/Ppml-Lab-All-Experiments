a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd_ab = x
x, y = gcd_ab, c
while y != 0:
    x, y = y, x % y
print("GCD of", a, b, c, "is", x)
