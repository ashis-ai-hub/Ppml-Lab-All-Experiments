s = input("Enter a string: ")
reverse_s = s[::-1]
print("Reversed string:", reverse_s)
if s == reverse_s:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
