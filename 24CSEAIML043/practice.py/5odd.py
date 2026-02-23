num = input("Enter a 5-digit number: ")
print("Digits at odd positions:")
for i in range(len(num)):
    if (i + 1) % 2 != 0:  
        print(num[i])
