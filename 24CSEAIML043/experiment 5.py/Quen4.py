l = []  
n = int(input("Enter the number of terms to be entered :"))
for i in range(n):
    i.append = int(input(f"enter {i+1}th number :"))
res = sorted(list(set(i)))
print("After removing the duplicate elements & sorting the list :",res) 
