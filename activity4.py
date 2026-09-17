try:
    pin = int(input("enter a 6 digit pin number: "))

    if len(pin) == 6:
        print("Valid PIN")
    else:
        print("Invalid PIN. Enter exactly 6 digits.")
except ValueError:
    print("Invalid PIN. Enter exactly 6 DIGITS.")