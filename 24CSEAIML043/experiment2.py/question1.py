p = float(input("Enter the principle amount:"))
r = float(input("Enter the rate of interest :"))
t = int(input("Enter the time:"))
n = int(input("Enter the number of compound per year:"))
a = int(input("Enter the final amount:"))
si = (p*t*r)/100
print("Simple interest is :",si)
a = p*(1 + r/100)**(n*t)
ci = a - p
print("Coumpound interest is :",ci)