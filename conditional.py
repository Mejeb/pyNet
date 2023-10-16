score = int(input("what was your test score?\n"))
age = int(input("What is your age?\n"))

if score >= 90:
    if age < 18:
        print("Your grade is A+")
    else:
        print("Your Grade is A")
elif score >= 80:
    if age < 18:
        print("Your grade is B+")
    else:
        print("Your Grade is B")
elif score >= 70:
    print("Your Grade is C")
else:
    print("Next time study more!")
