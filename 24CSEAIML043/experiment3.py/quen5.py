a = int(input("Enterc 1 st mark :"))
b = int(input("Enterc  2 nd mark :"))
c = int(input("Enterc 3 rd mark :"))
d = int(input("Enterc 4 th mark :"))
e = int(input("Enterc 5 th mark :"))
sum = a + b + c + d + e
percentage = (sum / 250) * 100
print("Percentage:", percentage)
if percentage >= 90 and percentage <= 100:
    print("Grade: O")
elif percentage >= 80 and percentage <= 90:
    print("Grade: E")
elif percentage >= 70 and percentage <= 80:
    print("Grade: A")
elif percentage >= 60 and percentage <= 70:
    print("Grade: B")
elif percentage >= 50 and percentage <= 60:
    print("Grade: C")
else:
    print("Grade: F")
