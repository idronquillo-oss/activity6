try:
    exam = int(input("Please enter your grade: ").lower())

    if 0 <= exam <= 100:
        print("Valid exam grade: ", exam)
    else:
        print("Invalid grade")

except ValueError:
    print("Invalid exam grade.")