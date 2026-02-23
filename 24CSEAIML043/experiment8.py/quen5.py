def primecheck(a):
    for i in range(2,a):
        if a % i ==0:
            return"not"
        else:
            return ""
a = int(input("Enter a number :"))
print(f"{a} is {primecheck(a)} a prime number")