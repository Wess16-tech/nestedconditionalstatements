medical_course = input("Do you have a medical course? (Y/N): ")
atten = int(input("Enter the attendance of the student: "))

if medical_course == "Y":
    print("You are allowed.")
else:
    if atten >= 75:
        print("Allowed.")
    else:
        print("Not allowed.")