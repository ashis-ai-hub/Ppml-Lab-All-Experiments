
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
add = a + b
sub = a - b
mul = a * b
div = a / b if b != 0 else "Undefined (division by zero)"
mod = a % b if b != 0 else "Undefined (modulus by zero)"
exp = a ** b
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Modulus:", mod)
print("Exponentiation:", exp)
