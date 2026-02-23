def si(p,t,r):
    return(p*t*r)/100
p = int(input("Enter a principle amount:"))
t = int(input("Enter the time:"))
r = int(input("Enter the rate if interest :"))
print("The sample interest is :",si(p,t,r))