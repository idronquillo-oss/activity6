import re

student_id = input("Enter student id: ")

pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern, student_id):
    print("Valid student id")
else:
    print("Invalid student id")