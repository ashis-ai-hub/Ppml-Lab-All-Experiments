
n = int(input("Enter a positive number: "))
if n< 0:
    print("factorial is not defined for negetive number ")
else:
    fact = 1
    i = 1
    while i <=n:
        fact*=i
        i +=1
    print("factorial :",fact)