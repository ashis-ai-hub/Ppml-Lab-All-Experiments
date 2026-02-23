fruits = ["apple", "banana", "mango", "orange", "grapes"]

print("Original List:", fruits)

print("\nList elements in reverse order:")
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])
print("\nLength of each fruit name:")
for fruit in fruits:
    print(fruit, "=", len(fruit))

reverse_fruits = []

for fruit in fruits:
    reverse_fruits.append(fruit[::-1])

print("\nList with reversed elements:")
print(reverse_fruits)
