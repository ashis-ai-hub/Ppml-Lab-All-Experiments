
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Before swapping: a =", a, "b =", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping: a =", a, "b =", b)
