# Input m and n
m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))

# Create list using for loop
list1 = []
for i in range(m, n + 1):
    list1.append(i)
print("List :",list1)
s = sum(list1)
print("Sum :",s)
print("Average :",s/len(list1))
print("Largest :",max(list1))
print("Smallest :",min(list1))
list2 = []
for x in list1:
    if x %3 != 0:
        list2.append(x)
print("Without divisible by 3 :",list2)
