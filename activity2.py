grade = int(input("Please enter your grade: ").lower())

if 0 <= grade <= 100:
    print("Valid grade:", grade)
else:
    print("Invalid grade")