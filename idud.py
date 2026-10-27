email = input("Enter email: ")
student_id = input("Enter student ID: ")
if "@" in email and "." in email:
    print("Email looks correct.")
else:
    print("Email is incorrect.")
if student_id.startswith("STU") and len(student_id) == 7:
    print("Student ID looks correct.")
else:
    print("Student ID is incorrect.")

