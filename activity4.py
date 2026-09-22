pin = (input("Create a 6 digit pin: "))

if len(pin) == 6 and pin.isdigit():
    print("Valid PIN")
else:
    print("Invalid PIN. Enter exactly 6 digits.")

