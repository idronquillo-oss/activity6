try:
    exam = int(input("Enter examination score: "))

    if 0 <= exam <= 100:
        print("Valid score: ", exam)
    else:
        print("Invalid score")

except ValueError:
    print("Invalid input. Please enter a number")