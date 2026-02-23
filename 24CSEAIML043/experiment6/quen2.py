
d1 = {}
n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value
d2 = {}
for key, value in d1.items():
    d2[value] = key
print("\nFirst Dictionary:")
print(d1)

print("\nSecond Dictionary (Keys and Values Swapped):")
print(d2)
