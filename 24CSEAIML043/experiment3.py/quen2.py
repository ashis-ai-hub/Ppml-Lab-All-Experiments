import math

a = int(input("Enter 1 number : "))
b = int(input("Enter 2 number : "))
c = int(input("Enter 3 number : "))

d = (b * b) - (4 * a * c)

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("Two real roots are:", r1, r2)

elif d == 0:
    r = -b / (2 * a)
    print("One real root is:", r)

else:
    print("No real roots")
