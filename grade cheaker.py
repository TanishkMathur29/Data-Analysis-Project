name = input("Enter your name : ")
Marks = int(input("Enter your marks : "))
if Marks >= 90:
    print("Grade A", name, "you are pass")
elif Marks >= 75:
    print("Grade B", name, "you are pass")
elif Marks >= 60:
    print("Grade C", name, "you are pass")

elif Marks >= 33:
    print("Grade D", name, "you are pass")
else:
    print("Grade F", name, "you are fail")