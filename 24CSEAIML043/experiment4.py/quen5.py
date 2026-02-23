
num = int(input("Enter a number: "))
on = num  # Store original number
rn = 0

while num > 0:
    d = num % 10
    rn = rn * 10 + d
    num = num // 10

if on == rn:
    print(f"{num}is a palindrome")
else:
    print(f"{num}is not a palindrome")
